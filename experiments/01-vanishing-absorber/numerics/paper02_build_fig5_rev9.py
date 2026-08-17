from pathlib import Path
import json
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
SUMMARY = ROOT / 'results/paper02_full_channel_rejection_summary.json'
OUTDIR = ROOT / 'paper02_figures'


def main():
    data = json.loads(SUMMARY.read_text())
    rows = data['rows']
    x = [r['max_frequency_hz'] / 1e9 for r in rows]
    root = [r['root_required_snr_db'] for r in rows]
    full = [r['full_required_snr_db'] for r in rows]

    OUTDIR.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(6.8, 4.6))
    ax.plot(x, root, marker='o', label='Root space')
    ax.plot(x, full, marker='s', linestyle='--', label='Full channel')
    ax.set_xlabel('Maximum RF frequency in joint fit (GHz)')
    ax.set_ylabel('Required RMS-channel SNR (dB)')
    ax.legend(frameon=False)
    ax.tick_params(labelsize=10)
    fig.tight_layout()
    fig.savefig(OUTDIR / 'fig5_required_snr_vs_bandwidth_rev9.pdf', bbox_inches='tight')
    fig.savefig(OUTDIR / 'fig5_required_snr_vs_bandwidth_rev9.png', dpi=300, bbox_inches='tight')
    plt.close(fig)


if __name__ == '__main__':
    main()
