from bs4 import BeautifulSoup as bs
import requests


def main():
	with open('input.txt', 'r') as file_input:
		Lines = file_input.readlines()

	for line in Lines:
		line_html = requests.get(line).text
		soup = bs(line_html, 'html.parser')
		title = soup.title.string[:-9]
		if soup.title.string == ' - YouTube':
			with open('output.txt', 'a+', encoding='utf-8') as file_output:
				file_output.write(f'Video Unavailable - {line}')
		else:
			with open('output.txt', 'a+', encoding="utf-8") as file_output:
				file_output.write(f'{title}- {line}')

	print(f'\x1b[6;30;42mTask Completed\x1b[0m')	

main()

