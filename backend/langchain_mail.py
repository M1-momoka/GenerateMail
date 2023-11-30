from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def create_mail(content):

    #一つ目のチェーン作成：メール内容の生成
    template="""
    あなたはビジネスマナーに精通した社会人です.与えられたメールの内容を元に、正しい敬語表現を利用したメールの文章を生成することがあなたの仕事です。
    メールの内容:{content}
    生成文章："""

    prompt = PromptTemplate(
        input_variables=["content"],
        template=template
    )

    chain1=LLMChain(
        llm=OpenAI(model_name="text-davinci-003",temperature=0,max_tokens=1000),
        prompt=prompt,
        output_key="modified_content"
    )

    #二つ目のチェーン作成：メールの件名の作成
    template="""
        メール本文をもとにこのメールの件名を教えてください。
        できるだけ具体的に、かつ端的にわかりやすくしてください。
        メール本文：
        {modified_content}
        件名："""  

    prompt = PromptTemplate(
        input_variables=["modified_content"],
        template=template
    )

    chain2=LLMChain(
        llm=OpenAI(model_name="text-davinci-003",temperature=0,max_tokens=1000),
        prompt=prompt,
        output_key="subject"
    )

    from langchain.chains import SequentialChain

    overall_chain=SequentialChain(
        chains=[chain1,chain2],
        input_variables=["content"],
        output_variables=["modified_content","subject"],
        verbose=True
    )
    result = overall_chain({"content": content})

    return result["modified_content"], result["subject"]