import re

def convert_novelai_to_webui(prompt: str) -> str:
    def replace_brackets(match, weight_increase, weight_decrease):
        text = match.group(1)
        if match.group(0).startswith('{'):
            weight = 1.05 ** weight_increase
        else:
            weight = 0.95 ** weight_decrease
        return f"({text}:{weight:.2f})"

    # 增强权重
    while re.search(r'\{([^{}]*)\}', prompt):
        prompt = re.sub(r'\{([^{}]*)\}', lambda m: replace_brackets(m, prompt.count('{'), 0), prompt)

    # 减弱权重
    while re.search(r'\[([^\[\]]*)\]', prompt):
        prompt = re.sub(r'\[([^\[\]]*)\]', lambda m: replace_brackets(m, 0, prompt.count('[')), prompt)
    
    prompt = re.sub(r'\s+', ' ', prompt).strip()
    
    return prompt

novelai_prompt = input("请输入NovelAI格式的提示词：")
converted_prompt = convert_novelai_to_webui(novelai_prompt)
print("转换后的WebUI提示词：", converted_prompt)
