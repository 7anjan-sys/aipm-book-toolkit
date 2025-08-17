#!/usr/bin/env python3
"""
Monte Carlo Velocity Simulator

Usage:
  python scripts/monte_carlo_velocity.py --velocities 18,22,20,19 --sprints 10000 --target 120

Outputs:
  - Summary stats to stdout
  - Optional histogram PNG if --plot is passed
"""
import argparse, random, statistics, json
from typing import List

def parse_velocities(s: str) -> List[float]:
    return [float(x.strip()) for x in s.split(",") if x.strip()]

def simulate(vels: List[float], sprints: int, target: float = None):
    samples = []
    for _ in range(sprints):
        samples.append(random.choice(vels))
    mean_v = statistics.mean(samples)
    p50 = statistics.median(samples)
    p90 = sorted(samples)[int(0.9*len(samples))-1]
    out = {"mean": mean_v, "p50": p50, "p90": p90}
    if target is not None and target > 0:
        # probability of reaching target over N future sprints can be added later
        pass
    return out, samples

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--velocities", required=True, help="Comma-separated historical velocities, e.g., 18,22,20,19")
    ap.add_argument("--sprints", type=int, default=10000)
    ap.add_argument("--plot", action="store_true")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    vels = parse_velocities(args.velocities)
    summary, samples = simulate(vels, args.sprints)

    print(json.dumps({"summary": summary}, indent=2))

    if args.plot:
        try:
            import matplotlib.pyplot as plt
            plt.hist(samples, bins=min(20, max(5, len(set(samples)))))
            plt.title("Velocity Simulation")
            plt.xlabel("Velocity")
            plt.ylabel("Frequency")
            plt.savefig("velocity_hist.png", bbox_inches="tight")
            print("Saved plot: velocity_hist.png")
        except Exception as e:
            print("Plotting failed:", e)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump({"summary": summary, "samples": samples[:1000]}, f, indent=2)

if __name__ == "__main__":
    main()
