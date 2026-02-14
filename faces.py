def convert(input_text):
    output_text = input_text
    if ":)" in output_text:
        output_text = output_text.replace(":)", "🙂")
    if ":(" in output_text:
        output_text =  output_text.replace(":(", "🙁")

    return output_text

txt= input()
outputxt= convert(txt)
print(outputxt)
#print(convert(input()))#
