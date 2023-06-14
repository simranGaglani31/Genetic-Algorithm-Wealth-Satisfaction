# Genetic-Algorithm-Wealth-Satisfaction
Description: This project explores the relationship between wealth and happiness. It implements an economic model to assess the amount of money required for achieving satisfaction. This repository provides a codebase that allows users to analyze and understand the relationship between income and happiness based on economic principles.
# Genetic Algorithm

This genetic algorithm solves the optimal investment pattern in the health care experiment. Below are the details of the experiment and the parameters used.

## General Aspects
1. There will be 10 periods. Players begin with 70 health.
2. Each period, the player harvests some amount of money (this amount is detailed below)
3. After harvesting, the player's health degenerates (this amount is detailed below)
4. After health degeneration, the player must spend money on Health Investments and Life Investments. Money spent on Health Investments increases health, while money spent on Life Investments gives the player Life Enjoyment. Any money not spent carries over into the next period.
5. A player dies if their health ever goes below 0. If a player dies, they receive 0 Life Enjoyment for the remaining periods.
The goal is to maximize total Life Enjoyment across all periods.

## Functions
 
### Harvesting:
1. The player earns income by harvesting black dots in a region designated by M x N cells. In our parameters (M = N = 100)
2. The player can select any set of contiguous W columns to harvest. In our parameters (W = 10)
3. When fully healthy, there are T black dots dispersed across M x W cells each period. Each black dot is worth v. In our parameters T = 100 and v = 1
4. The number of rows that can be harvested each period are given by: $ HarvestRows(H) = M(1-\gamma \frac{100 - H}{100}) $ where $\gamma = 1$
5. The number of rows are reduced by disabling the rows in the upper and lower regions of the selected columns.
6. With these parameters, if health is 50 at the start of the period, the player has only 500 cells in which they can harvest black dots. With 80 health, they have 800 cells.

### Degeneration:
Each period, the player loses (10 + CurrentPeriod) in health. i.e. 11 health the first period, 12 the second period, up to 20 in the last period.

### Health Regeneration:
The equation for the amount of health regained given a certain Health Investment, I, and health after harvesting, H, is given by: 

\begin{align}
HealthRegained(I, H) = 100 ( \frac{e^{k * I}}{e^{k * I} + \frac{100 - H}{H}}) - H
\end{align}

where (k = 0.01021).  Health cannot exceed 100, and is always rounded down to the nearest integer.


### Life Enjoyment:
The equation for the amount of Life Enjoyment given a certain Life Investment, L, is given by: 

\begin{align}
LifeEnjoyment(L, CurrentHealth) = c(\frac{CurrentHealth}{100})(\frac{L}{L + \alpha})
\end{align}

where (c = 464.53) and ($\alpha$ = 32).

CurrentHealth is the health the player has during the investment phase __INCLUDING__ the amount regained this period through investments in health.


I can change any of the following:

- Harvesting grid size, selection width, dot density, and dot value.
- Regeneration parameters
- Life Enjoyment parameters
- Number of Periods
- Degeneration per period

