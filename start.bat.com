@echo off
TITLE Ryuzaki bot
:: Enables virtual env mode and then starts Ryuzaki
env\scripts\activate.bat && py -m Ryuzaki
