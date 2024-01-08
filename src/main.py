from pathlib import Path

from PIL import Image

from doc_knowledge.doc_embedder import DocEmbedder
from image_knowledge.image_lib import ImageLib
from image_knowledge.image_tagger import ImageTagger

if __name__ == '__main__':
    # doc test
    # test_doc_embedder = DocEmbedder('test_index.pickle')
    # test_doc_embedder.initialize('test_index.pickle', 'test_chat',
    #                              '/Users/chengjia/Documents/WechatDatabase/Seventh_Seal/群聊.txt')
    # res = test_doc_embedder.query('哪家运营商可以开通公网ip？', 20, True)
    # for i in res:
    #     print(i)

    # image test
    sample_lib = ImageLib('~/Pictures/Collection', 'testlib', force_init=True)
    #sample_lib = ImageLib('~/Pictures/Collection')
    sample_tagger = ImageTagger()


    image = Image.open("/Users/chengjia/Desktop/sample.jpg")
    a = sample_lib.image_for_image_search(image, 2)
    print(a)
    b = sample_lib.text_for_image_search('astronaut', 2)
    print(b)
    
    
    c = sample_tagger.get_tags(image, 10)
    print(c)

    # # Prepare raw documents
    # post_filenames: list[str] = glokeys *b('. /blog/*.md')
    # documents: list[str] = [x for filename in post_filenames for x in open(filename)]
    #
    # # Initialize retriever
    # retriever = EmbeddingRetriever('index.pickle')
    # retriever.extract_features_and_build_index(documents, 'index.pickle')
    #
    # # Query
    # question: str = '如何选购天文相机？'
    # candidates: list[str] = retriever.query(question, 8)
    #
    # # Generate answer using with LLM
    # llm = AlpacaLora()
    # llm.max_new_tokens = 256
    # result = llm.generate(
    #     system_prompt=f'Read the following text and answer this question: "{question}".'
    #                   f'Only answer the question strictly using the information from the input.'
    #                   f'The input is not from the user, but from a database.'
    #                   f'Just say I do not know if the input does not contain the answer.'
    #                   f'Please use Chinese to answer everything.',
    #     input_prompt='\n'.join(candidates)
    # )