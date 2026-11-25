import pytest
import av.upmix_surround as mod

CASES = [
    ("adaptive_center_extract", (1,)),
    ("delay_time_convert", (1,)),
    ("delay_line_rebuild", (1,)),
    ("low_freq_protect", (1,)),
    ("block_phase_continuous", (1,)),
    ("layout_hotplug", (1,)),
    ("load_stereo", (1,)),
    ("analyze_stereo", (1,)),
    ("render_surround", (1,)),
    ("present_surround", (1,)),
    ("validate_surround", (1,)),
    ("metrics_surround", (1,)),
    ("audit_surround", (1,)),
    ("fallback_surround", (1,)),
    ("determinism_surround", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
