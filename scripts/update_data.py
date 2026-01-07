# 用于更新仓库的数据
# MIT LICENSE
import json
from pathlib import Path

DATA_PATH = Path("datas") / "v1"

def update_metadata(data: dict):
    with open(DATA_PATH / "metadata.json", "w", encoding="utf8") as f:
        json.dump({
            "last_update": data["metadata"]["timestamp"],
            "latest_episode": int(data["metadata"]["episode"]),
            "total": get_index_len()
        }, f, ensure_ascii=False)
    print("update metadata.json done")

def add_index(data: dict):
    with open(DATA_PATH / "episode" / "index.json", "r", encoding="utf8") as f:
        index = json.load(f)
    for item in index:
        if item["episode"] == int(data["metadata"]["episode"]):
            return
    index.append(
        {
            "episode": int(data["metadata"]["episode"]),
            "timestamp": data["metadata"]["timestamp"],
            "video_count": len(data["videos"])
        }
    )
    with open(DATA_PATH / "episode" / "index.json", "w", encoding="utf8") as f:
        json.dump(index, f, ensure_ascii=False)
    print("update index.json done")

def update_latest(data: dict):
    
    data.pop()
    with open(DATA_PATH  / "latest.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False)
    print("update latest.json done")

def add_new_json(data: dict):
    with open(DATA_PATH / "episode" / f"{int(data['metadata']['episode'])}.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False)
    print(f"update {data['metadata']['episode']}.json done")

def get_index_len():
    with open(DATA_PATH / "episode" / "index.json", "r", encoding="utf8") as f:
        return len(json.load(f))

def main():
    with open(Path("upload") / "new_data.json", "r", encoding="utf8") as f:
        new_data = json.load(f)
    as_new = new_data["upload_config"]["as_new"]
    add_index(new_data)
    update_metadata(new_data)
    if as_new:
        update_latest(new_data)
    else:
        print("skip update latest.json")
    add_new_json(new_data)
    print(f"update #{new_data['metadata']['episode']} done, total:{get_index_len()}")

if __name__ == "__main__":
    main()