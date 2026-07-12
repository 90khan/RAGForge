import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
)

from config.settings import HF_MODEL

from .base_provider import BaseProvider


class HuggingFaceProvider(BaseProvider):

    def __init__(self):

        if torch.backends.mps.is_available():
            self.device = torch.device("mps")
        elif torch.cuda.is_available():
            self.device = torch.device("cuda")
        else:
            self.device = torch.device("cpu")

        print(f"Using device: {self.device}")

        self.tokenizer = AutoTokenizer.from_pretrained(
            HF_MODEL,
            trust_remote_code=True,
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            HF_MODEL,
            trust_remote_code=True,
            torch_dtype=torch.float32,
        ).to(self.device)

        self.model.eval()

    def generate(
        self,
        prompt: str,
        max_new_tokens: int = 256,
    ) -> str:

        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
        )

        inputs = {
            k: v.to(self.device)
            for k, v in inputs.items()
        }

        with torch.inference_mode():

            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                temperature=0.0,
            )

        generated = outputs[0][inputs["input_ids"].shape[1]:]

        return self.tokenizer.decode(
            generated,
            skip_special_tokens=True,
        ).strip()