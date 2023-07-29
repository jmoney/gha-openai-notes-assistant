import argparse
import openai
import sys

if __name__ == "__main__":

    prog = argparse.ArgumentParser()
    prog.add_argument("--assistant", help="Notes Assistant", required=True, action="store", dest="assistant")
    prog.add_argument("--file", help="File to process", required=True, action="store", dest="file")
    args = prog.parse_args()

    with(open(args.file, "r")) as f:
        content = f.read()
        if args.assistant == "quarterly_review":
            with(open("./prompts/quarterly_summary.txt", "r")) as f:
                prompt_template = f.read()
                chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt_template.format(completed_tasks=content)}])
                print(chat_completion.choices[0].message.content)
        else:
            print("Unknown assistant")
            sys.exit(1)
