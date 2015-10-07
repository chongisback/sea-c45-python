import triagram


def test_open_file():
    triagram.open_file()


def test_is_triagram_dictionary():
    dictionary = triagram.open_file()
    assert(type(dictionary) == dict)


def test_length_of_story():
    story = triagram.write_story()
    words = story.split(" ")
    assert(len(words) >= 300)


def test_end_of_story():
    story = triagram.write_story()
    assert(story[-1] == "." or story[-1] == "?" or
           story[-1] == "!")
