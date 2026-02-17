# Password Evaluator

An advanced entropy-based password evaluator.

## Options

- `-h`, `--help`: show this help message and exit
- `-p`, `--password PASSWORD`: The password to evaluate

## Usage

Evaluates a single password via the command line

```bash
password_evaluator --password "asdf832#@@asdfIlN"
```

## Entropy Results

- Score <= 20: 'very weak'.
- Score <= 35: 'weak'.
- Score <= 59: 'moderate'.
- Score <= 127: 'strong'.
- Score > 127: 'unbreakable'.