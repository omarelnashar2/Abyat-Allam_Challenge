from backend.prompt_generator import get_description, generate_poem, analyze_poem, get_egaza, get_orwd
from backend.llm import get_llm_response


def get_response(*args):
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