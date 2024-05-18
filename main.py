def main(book_filename):
	book = read_book_contents(book_filename)
	word_count = get_word_count(book)
	print(f"--- Begin report of {book_filename} ---")
	print(f"{word_count} words found in the document")

	letter_count = get_letter_count(book)
	print_letter_count(letter_count)
	print("--- End report ---")


def read_book_contents(filename):
	with open(filename) as book:
		return book.read()


def get_word_count(contents):
	return len(contents.split())


def letter_sort_on(dict):
	return dict["num"]


def print_letter_count(letter_dict):
	letter_list = []
	for node in letter_dict:
		letter_list.append({
			'name': node,
			'num': letter_dict[node]
		})

	letter_list.sort(reverse=True, key=letter_sort_on)

	for item in letter_list:
		print(f"The '{item['name']}' character was found {item['num']} times")


def get_letter_count(contents):
	letter_dict = {}
	for c in contents.lower():
		if not c.isalpha():
			continue
		
		if c in letter_dict:
			letter_dict[c] += 1
		else:
			letter_dict[c] = 1

	return letter_dict


main("books/frankenstein.txt")