import pickle
import random
from PAM import PAM250




def main():
    size = 20  #size of population
    gap_penalty = -2
    sequences, k = read_sequences('data.txt')
    population, seq_lengths = initialize(sequences, k, size)
    # print("pop size ", len(population))
    # print(population)
    genetic_algorithm(population)


def read_sequences(path):
   k = 0
   sequences = []
   with open(path,'r') as reader:
       for text in reader:
         text= text.replace('\n','')
         text = text.upper()
         sequences.append(text)
         k+=1
   return sequences,k


def initialize(sequences,k,size):
    longest = 0
    seq_lengths = []
    for seq in sequences:
        if len(seq) > longest:
            longest = len(seq)
        seq_lengths.append(len(seq))
    print('longest ', longest)
    # print(seq_lengths)
    individual = []
    population = []
    for i in range(size):
        j= 0;
        for seq in sequences:
            gaps = longest - seq_lengths[j] #get the lenght of this sequence
            front_gaps = random.randint(0,gaps)
            end_gaps = gaps - front_gaps
            seq = ('-'*front_gaps) + seq + ('-' * end_gaps)
            #print(seq)
            j+=1
            individual.append(seq)
        #print('\n')
        population.append(individual)
        individual= []
    return population,seq_lengths

def sum_of_pairs(population,gap_penalty):
    dummy  = 1
    total_score = 0
    sequence_number = 0;
    score_array = []
    for sequences in population:
        for seq_1 in sequences:
            sequence_number+=1
            score = 0
            dummy = 0
            for seq_2 in sequences:
                if seq_1 is seq_2 or dummy < sequence_number:
                    dummy+=1
                else:
                    #print(seq_1, '   ', seq_2)
                    i= 0
                    i = int(i)
                    for letter_i  in seq_1:
                        try:
                            if(letter_i == '-' or seq_2[i] == '-'):
                                score+=gap_penalty;
                            else:
                                score +=PAM250[letter_i][seq_2[i]]
                            i+=1
                        except:
                            pass
                    # print(score)
                    total_score+= score
        # print('\n')
        dummy = 1
        sequence_number = 0
        score_array.append(total_score)
        total_score = 0;

    return score_array

def selection(population,sum,pr):  #select a individual according to its possibility
    p = 0
    p = random.randint(1, sum)
    #    print(p)
    c = 0
    while pr[c] < p:
        c += 1
    return (population[c])


def halves_of_populations(population,score_array):
    scored_population = []
    new_population = []
    index = int(0)
    for indiv in population:
        scored_population.append([indiv, score_array[index]])
        index += 1
    scored_population = sorted(scored_population, key=lambda a_entry: a_entry[1])
    scored_population.reverse()
    half_of_population = scored_population[:len(scored_population) // 2]
    other_half = scored_population[len(scored_population) // 2:]

    sum = 0
    pr = []
    # print("other half is ",other_half)
    for i in other_half:
        if(i[1] < 0):
            space = 1
        else:
            space = i[1]
        sum += space + 1
        pr.append(sum);
    return half_of_population,other_half,sum,pr


def check_region(individual,gap_penalty,threshold,region_threshold):
    default_start = len(individual[0])//4
    default_end = len(individual[0])//2
    start_index = 0
    end_index = 0
    region = False
    previous_start = default_start
    previous_end = default_end
    region_length = 0

    first_seq = individual[0]
    letter_index = 0
    for letter_1 in first_seq:
       score =0
       for seq in individual:
           if first_seq == seq:
               pass
           else:
                letter_2 = seq[letter_index]
                if (letter_1 == '-' or letter_2 == '-'):
                     score += gap_penalty;
                else:
                     score += PAM250[letter_1][letter_2]

       if(score > threshold):
            # print('the score is', score)
            if(region == True):
                end_index+=1
            else:
                # print('started')
                region = True
                start_index = int(letter_index)
                end_index = int(letter_index) +1
       elif(region == True) and (end_index - start_index  > region_length):
           #print('bigger')
           previous_start = start_index
           previous_end = end_index -1
           region_length = end_index - start_index
           region = False
       else:
           region = False
       letter_index += 1;

    if region_length > region_threshold:
        sequence = individual[0]
        sequence = sequence[previous_start:previous_end]
        return previous_start,previous_end
    else:
        return default_start,default_end




def reproduce(individual1,gap_penalty,threshold,region_threshold):
    start_index,end_index = check_region(individual1,gap_penalty,threshold,region_threshold)
    child = []
    temp = []

    for seq in individual1:
        region = seq[start_index:end_index]
        temp.append(region)

    index = 0
    head = ''
    tail = ''

    for seq in individual1:
        head = seq[:start_index]
        tail = seq[end_index:]
        head = swap_gaps(head)
        tail =swap_gaps(tail)
        seq = head + temp[index] + tail
        child.append(seq)
        index+=1;
    return child


def swap_gaps(seq):
    new_seq = ''
    seq = list(seq)
    index =0
    while index < len(seq):
        if seq[index] == '-':
            swap_direction = random.randint(0, 1)
            if swap_direction == 1 and index < len(seq)-1:
                temp = seq[index+1]
                seq[index+1] = seq[index]
                seq[index] = temp
            elif index >0:
                temp = seq[index - 1]
                seq[index- 1] = seq[index]
                seq[index] = temp

        index+=1

    for letter in seq:
        new_seq+= letter
    return new_seq

def best_individual(half_of_population):
    indiv = half_of_population[0]

    return indiv


def print_indiv(indiv):
    score  = indiv[1]
    indiv = indiv[0]
    for seq in indiv:
        print(seq)
    print('the score: ', score)
def best_among_best(indivs):
    score = 0
    best = indivs[0]

    for indiv in indivs:
        if indiv[1] >score:
            best = indiv
            score = indiv[1]
    return best




def genetic_algorithm(population):
    found = False
    iterarion = 0
    size = 20
    best_individuals = []
    gap_penalty = 0
    threshold = 3
    region_threshold = 1
    print("pop size ", len(population))
    print(population)


    while (iterarion < 1000):
        iterarion += 1
        if iterarion % 100 == 2:
            print("Generation Count : " + str(iterarion) + '\n')

        new_population = []
        score_array = sum_of_pairs(population, gap_penalty)
        half_of_population, other_half,sum,pr = halves_of_populations(population,score_array)
        best_indiv = best_individual(half_of_population)
        print_indiv(best_indiv)
        best_individuals.append(best_indiv)

        for x in half_of_population:
            child = reproduce(x[0],gap_penalty,threshold,region_threshold)
            new_population.append(child)

        for i in range(size//2):
            x = selection(other_half,sum,pr)
            y = selection(other_half,sum,pr)
            child = reproduce(x[0],gap_penalty,threshold,region_threshold)
            if child not in new_population:
                new_population.append(child)
            else:
                print('/////////////////////////exist')
                i -= 1

        population = new_population

    found = best_among_best(best_individuals)
    print("\n\n the best alignment")
    print_indiv(found)
    print("\n\n\n")

main()
