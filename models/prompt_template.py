from langchain.prompts import PromptTemplate

class RecipePromptTemplate(PromptTemplate):
    def __init__(self, recipe_parser, *args, **kwargs):
        template = "provide the user's requested recipe.\n{format_instructions}\n{query}"
        input_variables = ["query"]
        partial_variables = {"format_instructions": recipe_parser.get_format_instructions()}
        super().__init__(template=template, input_variables=input_variables, partial_variables=partial_variables, *args, **kwargs)