# Concept Overview (WIP / Outline)

### Motivation 

Memory in LLM applications enables structured extraction and organization of information over time. A practical example is [AI-assisted journaling](https://x.com/patrick_oshag/status/1876455619516911720), where an LLM can process daily input (e.g. audio, text) and extract structured data (sentiment, focus topics, action items) that can be used to generate actionable insights and follow-ups. 

![Memory Course App](img/example.png)

In this course, we will build an LLM assisted journaling app for this use case from scratch, fully open source, and simple enough to run privately / locally using LangGraph. 

### Memory Types

[Human long-term memory is divided into different types:](https://en.wikipedia.org/wiki/Long-term_memory)

- Procedural: Skills, habits, routines
- Episodic: Events, experiences
- Semantic: Facts, concepts, relationships

We can [map these onto different memory types in AI applications:](https://arxiv.org/pdf/2309.02427)

- Procedural: Prompts
- Episodic: Few shot examples
- Semantic: Long-term facts we want to remember

In particular, semantic memories can be [organized into collections or a fixed profile](https://langchain-ai.github.io/langgraph/concepts/memory/#semantic-memory). 

### Updating Modes

Memories can be updates in different ways, incluing:

* Hot Path: Creating memories during runtime
* Background: Creating memories as a separate background task

### Memory Types in Our Journalling App

* If the app detects an entry, it will enter the top flow of the diagram. Everything in this branch can be done "in the background" without blocking the user.
* If the user asks a question, it will enter the bottom flow of the diagram where memories are retrieved and used to condition immediate responses for the user.

![Memory Course App](img/memory_course_app.png)

## 1. Procedural Memory (System Prompts)
- Shown in RED in the diagram
- Acts as the "how to" instructions for the AI
- Contains extraction rules and processing guidelines
- Can be updated through direct feedback
- Example: Instructions for extracting todos, sentiment, and themes from journal entries

## 2. Episodic Memory (Few Shot Examples)
- Shown in GREEN in the diagram
- Specific examples of successful memory extractions
- Helps the AI understand patterns through concrete cases
- Can be refined based on user feedback
- Example: Sample journal entries and their correctly extracted structures

## 3. Semantic Memory (Long-term Storage)

### a) Semantic Memory Profile
- Fixed structure with predefined fields
- Stores user-specific information
- Example fields:
  - name
  - family
  - location
  - preferences
  - patterns

### b) Semantic Memory Collections
- Open-ended lists of extracted memories
- Organized by type (todos, ideas, etc.)
- Searchable using natural language
- Example collections:
  - Todo items
  - Ideas
  - Insights
  - Messages to draft

## System Flow
1. User inputs either a Journal Entry or Ask Question
2. Router directs the input appropriately
3. For journal entries:
   - Uses procedural and episodic memory to process input
   - Updates semantic memory (both profile and collections)
4. For questions:
   - Queries the semantic memory
   - Uses profile for context
   - Returns relevant memories

## Summary
This creates a complete system where:
- Instructions (procedural) guide the extraction
- Examples (episodic) improve accuracy  
- Collections and profile (semantic) store the knowledge
- All components can be updated and refined through feedback

