import argparse, time, yaml
from etl.extract import run_extract
from etl.transform import run_transform
from etl.model import run_model
from etl.utils.logging import get_logger
from etl.utils.io import save_json
logger = get_logger("pipeline")

def load_config(p): 
    import yaml
    with open(p,"r",encoding="utf-8") as f: return yaml.safe_load(f)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config/config.yaml")
    ap.add_argument("--batch-id", default=None)
    ap.add_argument("--extract", action="store_true")
    ap.add_argument("--transform", action="store_true")
    ap.add_argument("--model", action="store_true")
    ap.add_argument("--run-all", action="store_true")
    args = ap.parse_args()

    cfg = load_config(args.config)
    report = {"ok": True, "steps": {}}
    t0 = time.time()
    try:
        batch_id = args.batch_id
        if args.run_all or args.extract:
            t = time.time(); res = run_extract(cfg); batch_id = res["batch_id"]
            report["steps"]["extract"] = {"ok": True, "elapsed_sec": round(time.time()-t,2), **res}
        if args.run_all or args.transform:
            assert batch_id, "Missing batch_id (run extract first)"
            t = time.time(); res = run_transform(cfg, batch_id)
            report["steps"]["transform"] = {"ok": True, "elapsed_sec": round(time.time()-t,2), **res}
        if args.run_all or args.model:
            assert batch_id, "Missing batch_id (run extract first)"
            t = time.time(); res = run_model(cfg, batch_id)
            report["steps"]["model"] = {"ok": True, "elapsed_sec": round(time.time()-t,2), **res}
    except Exception as e:
        report["ok"] = False; report["error"] = str(e)
        logger.exception("Pipeline failed")
    report["elapsed_total_sec"] = round(time.time()-t0,2)
    save_json("docs/last_run_metrics.json", report)
    logger.info(f"Report saved to docs/last_run_metrics.json | ok={report['ok']}")
if __name__ == "__main__":
    main()

