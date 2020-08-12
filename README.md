# Definite-clause-theorem-prover

## How to run the program

`$ python3 a4.py`

### Example 1: light lamp 1

`kb> load kb.txt`

`kb> tell live_outside closed_circuit_breaker_1 up_switch_1 up_switch_2` 

`kb> infer_all`

### Example 1: light Lamp 2

`kb> load kb.txt`

`kb> tell live_outside closed_circuit_breaker_1 up_switch_3`

`kb> infer_all`

### Example 2: Energize power outlet 2

`kb> load kb.txt`

`kb> tell live_outside closed_circuit_breaker_2`

`kb> infer_all`
