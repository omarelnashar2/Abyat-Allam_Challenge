poem_qafias = ["غير محدد", "أ", "لأ", "إ", "ا", "ء", "ب", "ت", "ث", "ج", "ح", "خ",
               "د", "ذ", "ر", "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق",
               "ك", "م", "ن", "ه", "و", "ي"]


poem_topics = ["غير محدد",
'ابتهال',
'اعتذار',
'الاناشيد',
'جود وكرم',
'حزينه',
'حكمة',
'دينية',
'ذم',
'رثاء',
'رحمة',
'رومنسيه',
'سياسية',
'شوق',
'صبر',
'عتاب',
'عدل',
'غزل',
'فراق',
'مدح',
'نصيحة',
'هجاء',
'وطنيه']


poem_bahrs = ["غير محدد",
"البسيط",
"الطويل",
"الكامل",
"الخفيف",
"المتدارك",
"المتقارب",
"الرمل",
"الرجز",
"السريع",
"المجتث",
"المديد",
"المضارع",
"المقتضب",
"المنسرح",
"الهزج",
"الوافي",]

poem_eras= ["غير محدد",
'الأندلسي',
'الاسلامي',
'الاموي',
'الايوبي',
'الجاهلي',
'العباسي',
'العثماني',
'الفاطمي',
'المملوكي',
'الحديث']

available_models = ["Original ALLAM", "Fine-tuned ALLAM", "GPT4o"]

body_allam_original={
    "input": "",
	"parameters": {
		"decoding_method": "greedy",
		"max_new_tokens": 200,
		"repetition_penalty": 1
	},
	"model_id": "sdaia/allam-1-13b-instruct",
	"project_id": "58be8619-9dea-46b0-ab2b-ecc001d6a1ed"
}
body_allam_tuned={
    	"input": "",
    	"parameters": {
    		"decoding_method": "greedy",
    		"max_new_tokens": 512,
    		"repetition_penalty": 1
    	},
    	"moderations": {
    		"hap": {
    			"input": {
    				"enabled": True,
    				"threshold": 0.5,
    				"mask": {
    					"remove_entity_value": True
    				}
    			},
    			"output": {
    				"enabled": True,
    				"threshold": 0.5,
    				"mask": {
    					"remove_entity_value": True
    				}
    			}
    		}
    	}
    }
