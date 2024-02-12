import cmd
import yaml

LANDMARK_FILE = os.path.expanduser('~/.doko_landmarks')

class ExtendedNoteBook(NoteBook):
    def do_list_landmarks(self, arg):
        """List all available landmark keywords."""
        if os.path.exists(LANDMARK_FILE):
            with open(LANDMARK_FILE, 'r') as f:
                locationdata = yaml.safe_load(f)
            if locationdata:
                print("Available landmark keywords:")
                for keyword in locationdata.keys():
                    print("- " + keyword)
            else:
                print("No landmark keywords available.")
        else:
            print("Landmark file does not exist.")

if __name__ == "__main__":
    ExtendedNoteBook().cmdloop()
