run:
	# @pyuic5 -x ./QT/main.ui -o ./QT/main_ui.py
	@python main.py

ui:
	@pyuic5 -x ./QT/main.ui -o ./QT/main_ui.py
	