import unittest

class TestS3Storage(unittest.TestCase):
  
  def test_it_allow_store_media(self):
    #A arrange
    self.there_is_source_file("files/test.txt")
    storage = S3MediaStorage()    

    #A act
    storage.store(dest="tests/foo/boo.txt", source="files/test.txt")
    
    #A assert
    assert storage.contains(path="tests/foo/boo.txt")

if __name__ == '__main__':
    unittest.main() 
