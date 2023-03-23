import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')

# Task 1
synsets = wn.synsets('dish')
print("==All synsets for 'dish'==")
for synset in synsets:
    print(f"{synset.name()}: {synset.definition()}")

# Task 2
print("\n==Retrieve all noun and verb synsets for 'dish'==")
noun_synsets = wn.synsets('dish', pos=wn.NOUN)
verb_synsets = wn.synsets('dish', pos=wn.VERB)

# Print noun synsets with definitions and examples
print("\nNoun Synsets:")
for i, synset in enumerate(noun_synsets):
    print(f"{i + 1}. Definition: {synset.definition()}")
    examples = synset.examples()
    if examples:
        print(f"   Example: {examples[0]}")
    else:
        print("   No examples available.")

# Print verb synsets with definitions and examples
print("\nVerb Synsets:")
for i, synset in enumerate(verb_synsets):
    print(f"{i + 1}. Definition: {synset.definition()}")
    examples = synset.examples()
    if examples:
        print(f"   Example: {examples[0]}")
    else:
        print("   No examples available.")

# Task 3
print('== Synsets for the noun \'dish\' ==\n')
noun_synsets = wn.synsets('dish', pos=wn.NOUN)

# Print names, definitions, and examples of each synset
for synset in noun_synsets:
    print(f"Name: {synset.name()}")
    print(f"Definition: {synset.definition()}")

    # Print examples, if any
    examples = synset.examples()
    if examples:
        print("Examples:")
        for example in examples:
            print(f"- {example}")
    else:
        print("No examples found.")

# Task 4
print('\n\n==Print names, definitions, and examples of each synset for the \'dish\' verb==')
verb_synsets = wn.synsets('dish', pos=wn.VERB)

# Print names, definitions, and examples of each synset
for synset in verb_synsets:
    print(f"Name: {synset.name()}")
    print(f"Definition: {synset.definition()}")
    examples = synset.examples()
    if examples:
        print("Examples:")
        for example in examples:
            print(f"- {example}")
    else:
        print("No examples found.")
    print()

# Task 5
print('\n\n==Get the lemma and the given lemma name of any synset of the word "dish"==')

synsets = wn.synsets('dish')
synset = synsets[0]

lemma = synset.lemmas()[0]
lemma_name = lemma.name()

print("Lemma name:", lemma_name)
print("Synset definition:", synset.definition())

# Task 6

print("\n==Get all lower and higher concepts in the WordNet generic hierarchy of the first synset of the noun 'work'. "
      "Get the root hypernym of this concept. ==")

# Get the first synset for the noun "work"
work_synset = wn.synset('work.n.01')

# Get all the hyponyms (lower concepts) of the work synset
hyponyms = work_synset.hyponyms()

print("\nLower concepts of 'work.n.01':")
for hyponym in hyponyms:
    print(f"- Name: {hyponym.name()}")
    print(f"  Definition: {hyponym.definition()}")

# Get all the hypernyms (higher concepts) of the work synset
hypernyms = work_synset.hypernyms()

print("\nHigher concepts of 'work.n.01':")
for hypernym in hypernyms:
    print(f"- Name: {hypernym.name()}")
    print(f"  Definition: {hypernym.definition()}")

# Get the root hypernym of the work synset
root_hypernym = work_synset.root_hypernyms()

print("\nRoot hypernym of 'work.n.01':")
print(f"- Name: {root_hypernym[0].name()}")
print(f"  Definition: {root_hypernym[0].definition()}")

# Task 7
print("\n==Use WordNet to find out what substances 'wood is made of (use the first lemma of the noun) and what "
      "substances it is part of==")

# Get the first noun synset for "wood"
wood_synset = wn.synsets('wood', pos=wn.NOUN)[0]

# Get the hyponyms for "wood"
wood_hyponyms = wood_synset.hyponyms()
print("\nWood Hyponyms:")
for hyponym in wood_hyponyms:
    print(" - " + hyponym.name().split(".")[0])

# Get the substance meronyms for "wood"
wood_substance_meronyms = wood_synset.substance_meronyms()
print("\nWood Substance Meronyms:")
for meronym in wood_substance_meronyms:
    print(" - " + meronym.name().split(".")[0])

# Task 8
print("\n==Find an antonym for 'horizontal'==")
# get all synsets of the adjective "horizontal"
synsets = wn.synsets('horizontal', pos=wn.ADJ)

# iterate over all the synsets and their lemmas to find antonyms
for synset in synsets:
    for lemma in synset.lemmas():
        if lemma.antonyms():
            print(f"Antonym of 'horizontal': {lemma.antonyms()[0].name()}")
            break

# Task 9
print("\n==Show what actions are involved in the concept of 'eat'==")
synsets = wn.synsets('eat')
verb_synsets = [synset for synset in synsets if synset.pos() == 'v']
for synset in verb_synsets:
    print(f"{synset.name()}: {synset.definition()}")
    hypernyms = synset.hypernyms()
    hyponyms = synset.hyponyms()
    print("  Hypernyms:")
    for hypernym in hypernyms:
        print(f"    - {hypernym.name()}: {hypernym.definition()}")
    print("  Hyponyms:")
    for hyponym in hyponyms:
        print(f"    - {hyponym.name()}: {hyponym.definition()}")

# Task 10
print("\n==Get the synsets for 'bowl.n.02' and 'polyhedron.n.01'==")
bowl = wn.synset('bowl.n.02')
polyhedron = wn.synset('polyhedron.n.01')

# Get the lowest common hypernyms of the two synsets
common_hypernyms = bowl.lowest_common_hypernyms(polyhedron)

# Print the name and definition of the smallest common hyponym
if common_hypernyms:
    smallest_common_hyponym = common_hypernyms[0]
    print("Smallest common hyponym:", smallest_common_hyponym.name())
    print("Definition:", smallest_common_hyponym.definition())
else:
    print("No common hyponyms found.")

# Task 11
print("\n==Get the synsets for 'bowl.n.01' and 'polyhedron.n.01'==")
bowl = wn.synset('bowl.n.02')
polyhedron = wn.synset('polyhedron.n.01')

# Get the lowest common hypernyms of the two synsets
common_hypernyms = bowl.lowest_common_hypernyms(polyhedron)

# Print the name and definition of the smallest common hyponym
if common_hypernyms:
    smallest_common_hyponym = common_hypernyms[0]
    print("Smallest common hyponym:", smallest_common_hyponym.name())
    print("Definition:", smallest_common_hyponym.definition())
else:
    print("No common hyponyms found.")

# Task 13
print("\n==Determine the semantic distance between the job.n.07 and work.n.01 synsets==")
job_synset = wn.synset('job.n.07')
work_synset = wn.synset('work.n.01')

distance = job_synset.path_similarity(work_synset)

print("Semantic distance between 'job.n.07' and 'work.n.01':", distance)

# Task 14
print("\n==Determine the semantic distance between the job.n.07 and work.n.07 synsets==")
job_synset = wn.synset('job.n.07')
work_synset = wn.synset('work.n.07')

distance = job_synset.path_similarity(work_synset)

print("Semantic distance between 'job.n.07' and 'work.n.07':", distance)

# Task 15
print("\n==Determine the semantic distance between the job.n.07 and entity.n.01 synsets==")
job_synset = wn.synset('job.n.07')
work_synset = wn.synset('entity.n.01')

distance = job_synset.path_similarity(work_synset)

print("Semantic distance between 'job.n.07' and 'entity.n.01':", distance)
