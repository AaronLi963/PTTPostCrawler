run:
	@pyuic5 -x ./QT/main.ui -o ./QT/main_ui.py
	@python3 main.py

ui:
	@pyuic5 -x ./QT/main.ui -o ./QT/main_ui.py

py:
	@python3 main.py