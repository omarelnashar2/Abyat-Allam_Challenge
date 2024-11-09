def get_description(poem):
    """
    Generates a prompt to summarize the given poem in simple meanings.

    Args:
        poem (str): A string representing the poem to be summarized.

    Returns:
        str: A prompt in Arabic asking for a simple summary of the poem. If the poem is empty or None, an empty string is returned.

    Example:
        description = get_description("قصيدة عن الحب والمشاعر")
        # Returns: "لخص القصيدة بمعاني بسيطة:\n قصيدة عن الحب والمشاعر"
    """
    if not poem:
        return ""
    
    prompt = f"لخص القصيدة بمعاني بسيطة:\n {poem}"
    return prompt


def generate_poem(context, topic, bahr, qafia, num_abyat, era):
    """
    Generates a prompt to write a poem based on the provided parameters, such as context, topic, bahr,
     qafia, number of poetrys (num_abyat), and the era.

    Args:
        context (str): Context or background information to help guide the poem's theme.
        topic (str): The main subject of the poem.
        bahr (str): The bahr to be used in the poem.
        qafia (str): The qafia to be used in the poem.
        num_abyat (int): The number of poetrys (lines) for the poem.
        era (str): The historical or cultural era for the poem's style.

    Returns:
        str: A prompt to generate a poem based on the given parameters. If certain parameters are missing or 
              set to "غير محدد", appropriate placeholders are used. If the required parameters are not met,
              an empty string or a simplified prompt is returned.

    Example:
        prompt = generate_poem("تفاصيل عن الفضاء", "الحب", "الطويل", "الميم", 5, "الحديث")
        # Returns a prompt for generating a poem based on the given details.
    """
    context = context.replace("غير محدد", "")
    topic = topic.replace("غير محدد", "")
    bahr = bahr.replace("غير محدد", "")
    qafia = qafia.replace("غير محدد", "")
    era = era.replace("غير محدد", "")
  
    if (context and not topic):
        return ""
    
    if all([topic, bahr, qafia, era]) and not all([context, num_abyat]):
        prompt = f"اكتب قصيدة عن موضوع {topic} وببحر {bahr} وبقافية {qafia} وبالعصر {era}: \n "    
    else:
        if num_abyat:
            if num_abyat <= 10 and num_abyat > 2:
                num_abyat = f"لا تزيد عن {str(num_abyat)} ابيات"
            else:
                num_abyat = f"لا تزيد عن {str(num_abyat)} بيت"
        
        if era:
            era = f"من العصر {era}"
            
        if bahr:
            bahr = f"من بحر {bahr}"
        
        if qafia:
            qafia = f"باستخدام قافية {qafia}"
            
        prompt = f"""
        اكتب قصيدة من تأليفك
        {topic} {context}
        {era}
        {num_abyat}
        {bahr}
        {qafia}
        اكتب القصيدة فقط بدون اي اضافات قبلها او بعدها
        """   
    return prompt


def analyze_poem(poem):
    """
    Generates a prompt to analyze the given poem.

    Args:
        poem (str): The poem (in Arabic) to be analyzed.

    Returns:
        str: A prompt in Arabic asking for an analysis of the poem. If the poem is empty or None, an empty string is returned.

    Example:
        analysis_prompt = analyze_poem("قصيدة عن النيل")
        # Returns: "قم بتحليل الابيات الشعرية الاتية: \n قصيدة عن النيل \n "
    """
    if not poem:
        return ""
    
    prompt = f"قم بتحليل الابيات الشعرية الاتية: \n {poem} \n "
    return prompt



def get_egaza(bayte):
    """
    Generates a prompt to validate or confirm the correctness of a given poetry.

    Args:
        bayte (str): A line or poetry from a poem to be validated.

    Returns:
        str: A prompt in Arabic asking to validate the correctness of the given poetry. If the poetry is empty or None, an empty string is returned.

    Example:
        egaza_prompt = get_egaza("بيت شعري")
        # Returns: "أجز قولي: \n {بيت شعري} \n "
    """
    if not bayte:
        return ""
    
    prompt = f"أجز قولي: \n {bayte} \n "
    return prompt


def get_orwd(bayte):
    """
    Generates a prompt to analyze or break down the metrical structure of a given poetry.

    Args:
        bayte (str): A line or poetry from a poem to be analyzed for its metrical structure.

    Returns:
        str: A prompt in Arabic asking for the metrical breakdown (i.e., the "taqti'a") of the Poetry. If the poetry is empty or None, an empty string is returned.

    Example:
        orwd_prompt = get_orwd("بيت شعري")
        # Returns: "قم بتقطيع هذا البيت عروضيا\n {بيت شعري} \n "
    """
    if not bayte:
        return ""
    
    prompt = f"قم بتقطيع هذا البيت عروضيا\n {bayte} \n "
    return prompt
