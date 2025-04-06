# Monte Carlo Pi Estimation
This project uses a **Monte Carlo simulation** to estimate the value of π. Wanted to try this project after reading *Fooled by Randomness* by Nicolas Nassim Taleb.

## How It Works
- Randomly throw points inside a square
- Count how many land inside the inscribed circle
- Use the ratio to estimate π

![Monte Carlo Simulation](monte-carlo.gif)

## Running the Code
To run the simulation:

Run the code:
```sh
git clone https://github.com/clrsims/monte-carlo-pi.git
cd monte-carlo-pi
python monte_carlo_pi.py
