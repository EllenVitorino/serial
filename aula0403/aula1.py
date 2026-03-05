import argparse
import hashlib
import math
import os
import time
from multiprocessing import Event, Process, Queue
def fmt_seconds(seconds: float) -> str:
if not math.isfinite(seconds):
return "infinito"
if seconds 0 else float("inf")
total = 10 ** n_digitos
tempo_estimado = total / hash_por_segundo if hash_por_segundo > 0 else float("inf")
return tempo_estimado, hash_por_segundo
def worker(
hash_bytes: bytes,
n_digitos: int,
inicio_faixa: int,
fim_faixa: int,
encontrado: Event,
resultado_queue: Queue,
):
for tentativa in range(inicio_faixa, fim_faixa):
if tentativa % 4096 == 0 and encontrado.is_set():
return
senha = f"{tentativa:0{n_digitos}d}".encode("ascii")
if hashlib.md5(senha).digest() == hash_bytes:
encontrado.set()
resultado_queue.put(senha.decode("ascii"))
return
def brute_force_parallel(hash_alvo: str, n_digitos: int, workers: int):
hash_bytes = bytes.fromhex(hash_alvo)
total = 10 ** n_digitos
if workers total:
workers = total
inicio = time.perf_counter()
resultado_queue = Queue()
encontrado = Event()
base = total // workers
resto = total % workers
blocos = []
inicio_bloco = 0
for i in range(workers):
tamanho = base + (1 if i inicio_faixa
]
for p in procs:
p.start()
for p in procs:
p.join()
tempo_total = time.perf_counter() - inicio
senha = resultado_queue.get() if not resultado_queue.empty() else None
return senha, tempo_total, len(procs)
def parse_workers(raw: str):
itens = [x.strip() for x in raw.split(",") if x.strip()]
workers = []
for item in itens:
valor = int(item)
if valor > 0:
workers.append(valor)
return workers or [12, 8, 4, 2]
def main():
parser = argparse.ArgumentParser(
description="Brute force MD5 para senha numérica de 9 dígitos (serial e paralelo)."
)
parser.add_argument(
"--hash",
required=True,
dest="hash_alvo",
help="Hash MD5 alvo (32 hex).",
)
parser.add_argument(
"--digits",
type=int,
default=9,
help="Quantidade de dígitos da senha (padrão: 9).",
)
parser.add_argument(
"--workers",
default="12,8,4,2",
help="Lista de workers separados por vírgula. Ex.: 12,8,4,2 (ordem de execução).",
)
parser.add_argument(