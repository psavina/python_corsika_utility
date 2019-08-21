# python_corsika_utility
python scripts for the generation and management of CORSIKA shower simulations.

## main
Main folder with the binary files:

- **generator**. Script for the generation of CORSIKA stearing cards and jobs for the batch queuing system;
- **controller**. Script that controls the simulations results and regenerate the failed simulations.

## showerGenerator
A package that handles the stearing cards generation.
-- randLib: used for the generation of the random numbers following the correct distributions-
-- primes.dat: prime numbers between 1901 and 45077

## corsikaDatacard
A package that handles the CORSIKA datacard structure.

## myOptions
A package that handles the options of the binaries.
