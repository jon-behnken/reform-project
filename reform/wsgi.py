import reform
import waitress

if __name__ == "__main__":
    waitress.serve(reform.create_app(), port=8080)
