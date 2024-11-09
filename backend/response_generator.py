from backend.prompt_generator import get_description, generate_poem, analyze_poem, get_egaza, get_orwd
from backend.llm import get_llm_response


def get_response(*args):
    """
    This function generates a response based on the provided arguments, which are used to construct 
    a prompt for different types of actions: poem generation, poem analysis, "egaza", or "orwd". 
    The function processes the arguments and uses a specified model to return the corresponding response.

    Args:
        *args: A variable length argument list. The function expects the following arguments:
            - The last two arguments should specify the model and the action type (e.g., "generate", "analysis", "egaza", "orwd").
            - For "generate", the previous eight arguments are used as parameters for generating a poem.
            - For "analysis", the previous three arguments are used for poem analysis and potentially additional description generation.
            - For "egaza" and "orwd", the previous three arguments are used for generating responses related to "egaza" and "orwd", respectively.

    Returns:
        str: The generated response from the specified model. The function interacts with external functions 
             (e.g., `generate_poem`, `get_llm_response`, `analyze_poem`, `get_description`, `get_egaza`, `get_orwd`) 
             to construct prompts and retrieve the response from the model.

    Notes:
        - The model argument is the second to last argument.
        - The action argument (e.g., "generate", "analysis", "egaza", "orwd") determines which block of code is executed.
        - The function expects specific numbers of arguments depending on the action. Incorrect arguments may lead to errors.
    """
    model = args[-2]
    if args[-1] == "generate":
        prompt = generate_poem(args[-8], args[-7], args[-6],
                               args[-5], args[-4], args[-3])
        return get_llm_response(prompt, model)
    
    elif args[-1] == "analysis":
        prompt = analyze_poem(args[-3])
        if model == "Fine-tuned ALLAM":
            description_prompt = get_description(args[-3])
            answer = get_llm_response(prompt, model)
            answer += "\n\n" + get_llm_response(description_prompt, model)
            return answer
        else:
            return get_llm_response(prompt, model)
    
    elif args[-1] == "egaza":
        prompt = get_egaza(args[-3])
        return get_llm_response(prompt, model)
    
    elif args[-1] == "orwd":
        prompt = get_orwd(args[-3])
        return get_llm_response(prompt, model)
    
    else:
        return
