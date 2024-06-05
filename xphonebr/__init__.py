import os
import requests
from tqdm import tqdm
from dp.phonemizer import Phonemizer as ph
import warnings
from .Util.norm import normalizer
import torch

# Suprimir o aviso específico
warnings.filterwarnings(
    "ignore",
    message="enable_nested_tensor is True, but self.use_nested_tensor is False because encoder_layer.self_attn.batch_first was not True",
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class Phonemizer:
    def __init__(self, autoreg=False, normalizer=False):
        self.model_path = self.download_model(autoreg)
        self.phones = ph.from_checkpoint(self.model_path, device=device)
        self.norm = normalizer

    def download_model(self, autoreg):
        base_url = "https://huggingface.co/traderpedroso/phonemizerBR/resolve/main/"
        model_name = "autoreg_transformer.pt" if autoreg else "transformer.pt"
        model_path = os.path.join("source", model_name)

        # Criar diretório se não existir
        os.makedirs("source", exist_ok=True)

        # Verificar e baixar o modelo se ele não existir
        if not os.path.exists(model_path):
            print(f"Downloading model {model_name}...")
            url = base_url + model_name
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Assegura que não ocorram erros no download

            total_size_in_bytes = int(response.headers.get("content-length", 0))
            block_size = 1024  # 1 Kibibyte

            progress_bar = tqdm(total=total_size_in_bytes, unit="iB", unit_scale=True)
            with open(model_path, "wb") as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
            progress_bar.close()

            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                print("ERROR, something went wrong")
            print("Download completed successfully.")
        else:
            print("Model already exists.")

        return model_path

    def phonemise(self, text):
        if isinstance(text, list):
            # Se for uma lista, normalizar e fonemizar cada item
            if self.norm:
                text = [normalizer(t) for t in text]
            return self.phones.phonemise_list(text, lang="pt_br")
        else:
            # Se for uma string, normalizar e fonemizar diretamente
            if self.norm:
                text = normalizer(text)
            return self.phones(text, lang="pt_br")
