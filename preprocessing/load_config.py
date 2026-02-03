import os
import yaml
#====================
#config.yamlを読み取り、dictを返す関数
#====================

def load_config(config_path: str) -> dict:
    if not isinstance(config_path, str) or not config_path:             # config_path が str型かどうか をチェック
        raise ValueError("config_path must be a non-empty string")      # もし None や int や list が来たらダメなのでエラーにする
    
    config_path = os.path.abspath(os.path.expanduser(os.path.expandvars(config_path)))     
    #=============================================================================================
    # os.path.expandvars(config_path):例："%USERPROFILE%/config.yaml" → "C:/Users/you/config.yaml"
    # os.path.expanduser(...): 例："~/config.yaml" → "C:/Users/you/config.yaml"（環境による）
    # os.path.abspath(...): 例："config.yaml" → "C:/Users/.../config.yaml"（今の作業フォルダ基準）
    #=============================================================================================
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"config.yaml not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)                             # YAMLを Python のデータ構造に変換する.LOG_DIR: "E:/logs"->{"paths": {"LOG_DIR": "E:/logs"}}

    if cfg is None:                          # 空ファイルなどの対策（None → {}）
        cfg = {}

    if not isinstance(cfg, dict):            # トップレベルが dict か確認
        raise ValueError("config.yaml top-level must be a mapping (dict)")

if __name__ == "__main__":
    cfg = load_config("config.yaml")
    print(cfg)
    # 例: cfg["paths"]["LOG_DIR"] を使う