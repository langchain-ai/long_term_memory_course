def format_few_shot_examples(examples):
    """ Format episodic memories for few shot examples"""
    formatted_examples = []
    for example in examples:
        formatted_examples.append(
            f"Input:\n{example.value['input']}\n\n"
            f"Output:\n{example.value['output']}\n"
        )
    return "\n---\n".join(formatted_examples)