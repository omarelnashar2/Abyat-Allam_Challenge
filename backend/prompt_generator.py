def get_description(poem):
    if not poem:
        return ""
    
    prompt = f"لخص القصيدة بمعاني بسيطة:\n {poem}"
    return prompt


def generate_poem(context, topic, bahr, qafia, num_abyat, era):
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
    if not poem:
        return ""
    
    prompt = f"قم بتحليل الابيات الشعرية الاتية: \n {poem} \n "
    return prompt


def get_egaza(bayte):
    if not bayte:
        return ""
    
    prompt = f"أجز قولي: \n {bayte} \n "
    return prompt


def get_orwd(bayte):
    if not bayte:
        return ""
    
    prompt = f"قم بتقطيع هذا البيت عروضيا\n {bayte} \n "
    return prompt
