import utils
from git import Repo 

def install_kuma():
    Repo.clone_from("https://github.com/louislam/uptime-kuma", "uptime-kuma")