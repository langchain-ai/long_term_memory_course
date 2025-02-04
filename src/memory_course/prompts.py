

# Instructions for memory collection extraction
memory_collection_extraction_instructions = """
You are a helpful assistant that extracts memories from a journal entry for a user.

<Instructions>
Given a journal entry, analyze and extract the following elements:

1. SENTIMENT:
   - Identify the overall emotional tone (positive, negative, neutral)
   - Note any significant emotional shifts or patterns
   - Extract key emotional words or phrases
   Output as a single memory with memory_type "SENTIMENT"

2. TODOS:
   - Extract each task, action, or commitment as a SEPARATE memory
   - Each TODO should be its own Memory object with memory_type "TODO"
   - Include deadline in the memory_content if mentioned
   - Format each todo concisely and clearly

3. IDEAS:
   - Extract each creative thought, insight, or potential project as a SEPARATE memory
   - Each idea should be its own Memory object with memory_type "IDEA"
   - Keep each idea focused and specific
   - Include any relevant details or requirements with that specific idea

Important: Create a new Memory object for EACH individual todo and idea. Do not combine multiple todos or ideas into a single memory.
</Instructions>"""

# Define the prompt for memory collection extraction input
collection_extraction_input = """
<Instructions>
{procedural_memory_instructions}
</Instructions>

<Few Shot Examples>
{few_shot_examples_formatted}
</Few Shot Examples>"""

# Define the prompt for updating the memory extraction instructions per feedback
update_memory_collection_extraction_instructions = """
You goal is examine user feedback on an extraction task and use that to update the instructions.

<Current Instructions>
{instructions}
</Current Instructions>

Produce new instructions that incorporate the user feedback. Add no preamble or postamble.

Retain the original instructions as a base and only update the instructions that need to be changed."""

# Define the prompt for updating the few shot examples per feedback
update_few_shot_examples_instructions="""
You are an expert at creating few-shot examples based on user feedback.
Here are the current few shot examples to use for formatting (if they are present):

<Current Few-Shot Examples>
{current_examples}
</Current Few-Shot Examples>

<Instructions>
1. Review the user feedback:
2. Create new examples based upon the user feedack 
3. Maintain the same format as the existing examples, if they are present 

Do not:
- Add explanatory text or commentar
</Instructions>

Output only the new examples:
"""

# Define the prompt for searching for memories in a given collection
memory_search_instructions = """

<Instructions>
You are a helpful assistant that can search for memories in a given collection.

Your goal is to determine which collection the user is interested in searching.

You will be given a list of available collections, a user input, and the prompt used for memory classification so that you have full context on how memories are classified.

Your job is to return the name of the collection that best matches the user input.
</Instructions>

<Available Collections>
{available_collections}
</Available Collections>

<Memory Classification Prompt>
{memory_classification_prompt}
</Memory Classification Prompt>
"""

# Define the prompt for extracting a user profile from a journal entry
profile_extraction_input = """

<Instructions>
{memory_profile_extraction_instructions}
</Instructions>

<Existing Profile>
{profile}
</Existing Profile>

<USER JOURNAL ENTRY>
{journal_entry}
</USER JOURNAL ENTRY>
"""

# Define the prompt for extracting a user profile from a journal entry
memory_profile_extraction_instructions = """
You are a helpful assistant that extracts a user profile.

<Instructions>
Given a journal entry and, optionally, an existing user profile, create or update the fields of the user profile.

Keep any existing fields of the user profile that are not mentioned in the journal entry. 

Do not forget information. 

If the journal entry mentions new information relevant to the fields, then populate them. 

If the journal entry updates information in any of the fields, then update them.

</Instructions>"""

# Define the prompt for routing a user request
routing_instructions = """
<Instructions>      
Take a user request and classify it into one of the following categories:

- search: The user is asking to retrieve or find information from their existing journal entries
    Example: "Show me entries about project work"
    Example: "Find times when I mentioned feeling stuck"

- extract: The user is submitting a new journal entry that needs to be processed
    Example: "Today I made great progress on the API design"
    Example: "Dear journal, just finished a productive meeting"

- update_instructions: The user is providing general rules about what information to extract from entries
    Example: "Extract each creative thought, insight, or potential project as a SEPARATE memory and classify it as IDEA"
    Example: "Identify the overall emotional tone (positive, negative, neutral) and classify it as SENTIMENT"

- update_examples: The user is providing specific classification examples 
    Example: "It would be cool to build an open source journal as an example of an IDEA"
    Example: "I need to take out the trash tomorrow is an example of a TODO"
</Instructions>
"""