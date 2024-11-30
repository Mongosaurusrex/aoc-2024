setup: 
	poetry env use 3.11.8
	poetry install
start: setup
	poetry shell
splash_screen:
	@cat christmas.txt
	@echo "---------------------------------------------------------------------------"
merry-christmas: splash_screen
	@python main.py
	@echo "---------------------------------------------------------------------------"
	@cat santa.txt
