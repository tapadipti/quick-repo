import random, time, os, json
from dvclive import Live

with Live(save_dvc_exp=True) as live:
    epochs = int(1 + random.random() * 10)
    live.log_param("epochs", epochs)
    for i in range(epochs):
        live.log_metric("foo", i + random.random())
        live.log_metric("bar", epochs - (i + random.random()))
        live.log_metric("nested/bar", epochs - (i + random.random()))
        live.next_step()
        # time.sleep(1)

metrics_dict = {"metric-1": random.random(), "metric-2": epochs - random.random()}
OUTPUT_DIR = "output"
METRICS_FILE = os.path.join(OUTPUT_DIR, "metrics.json")
with open(METRICS_FILE, "w") as f:
    f.write(json.dumps(metrics_dict))