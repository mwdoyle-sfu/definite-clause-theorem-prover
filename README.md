# Definite-clause-theorem-prover

Definite clauses are a subset of the regular propositional calculus. A knowledge base file (KB file for short) consists of 1, or more, rules. The system can infer which rules hold true based on the truth variables and the rules the user provides. See below for an example of energizing circuits in a house.

## How to run the program

`$ python3 dctp.py`

### Example 1: light lamp 1

```
kb> load kb.txt

kb> tell live_outside closed_circuit_breaker_1 up_switch_1 up_switch_2

kb> infer_all
```

### Example 1: light Lamp 2

```
kb> load kb.txt

kb> tell live_outside closed_circuit_breaker_1 up_switch_3

kb> infer_all
```

### Example 2: Energize power outlet 2

```
kb> load kb.txt

kb> tell live_outside closed_circuit_breaker_2

kb> infer_all
```

### Circuit Diagram

![alt text](https://github.com/mwdoyle-sfu/definite-clause-theorem-prover/blob/master/diagram.png?raw=true)
