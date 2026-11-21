# Changelog: what we changed since Milestone 1

## [1/11/2026] Test set and checking script
- Added 10 C++ test programs with the correct output from a real C++ run (test-data/tests)
- Added code/run.py, which runs each Python translation and compares it with the C++ output

## [8/11/2026] V0, the plain prompt
- Ran the plain prompt on all 10 programs: 4 of 10 passed

## [8/11/2026] V1, the better prompt (P1)
- Added a role, rules, a checklist of 7 C++ habits, one example and a request for short notes: 9 of 10 passed (T05 crashed)

## [15/11/2026] V2, the repair prompt (P2)
- Showed Claude the failed test, the expected output and the real error: 10 of 10 passed

## [17/11/2026] Documents and prototype
- Added the diagrams, the Colab notebook, the README and the Milestone 2 PDF
