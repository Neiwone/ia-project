import tkinter as tk
import csv
from tkinter import ttk, messagebox
from models.candidate import Candidate, Person
from classifier.classifier import Classifier

def load_candidates_from_file(file_path):
    candidates = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            # Ignorar o cabeçalho
            next(reader, None)

            for row in reader:
                if len(row) != 8:
                    print(f"Erro no formato dos dados: {row}")
                    continue

                name, age, email, experience, soft_skills, hard_skills, team_work, problem_solving = row

                try:
                    person = Person(name, int(age), email)
                    candidate = Candidate(
                        person,
                        experience.strip(),
                        soft_skills.strip(),
                        hard_skills.strip(),
                        team_work.strip(),
                        problem_solving.strip(),
                    )
                    candidates.append(candidate)
                except ValueError as e:
                    messagebox.showerror("Erro", "Erro ao tentar criar candidato")
            messagebox.showinfo("Sucesso", "Candidato adicionado com sucesso!")

    except FileNotFoundError:
        messagebox.showerror("Erro", f"Arquivo {file_path} não encontrado")
    except Exception as e:
        messagebox.showerror("Erro", e)

    return candidates


class App:
    def __init__(self):
        self.candidates = []
        self.root = tk.Tk()
        self.root.title("Sistema de Cadastro de Candidatos")

        self.create_form()
        self.create_buttons()
    
    def set_candidates(self):
        self.candidates = load_candidates_from_file('chat-gpt\candidates.csv')

    def create_form(self):
        # Criar o formulário de entrada
        self.form_frame = ttk.Frame(self.root, padding="10")
        self.form_frame.grid(row=0, column=0, sticky="EW")

        # Nome
        name_label = ttk.Label(self.form_frame, text="Nome:")
        name_label.grid(row=0, column=0, sticky="W")
        self.name_entry = ttk.Entry(self.form_frame)
        self.name_entry.grid(row=0, column=1, sticky="EW")

        # Idade
        age_label = ttk.Label(self.form_frame, text="Idade:")
        age_label.grid(row=1, column=0, sticky="W")
        self.age_entry = ttk.Entry(self.form_frame)
        self.age_entry.grid(row=1, column=1, sticky="EW")

        # Email
        email_label = ttk.Label(self.form_frame, text="Email:")
        email_label.grid(row=2, column=0, sticky="W")
        self.email_entry = ttk.Entry(self.form_frame)
        self.email_entry.grid(row=2, column=1, sticky="EW")

        # Experiência
        experience_label = ttk.Label(self.form_frame, text="Experiência:")
        experience_label.grid(row=3, column=0, sticky="W")
        self.experience_entry = ttk.Entry(self.form_frame)
        self.experience_entry.grid(row=3, column=1, sticky="EW")

        # Soft Skills
        soft_skills_label = ttk.Label(self.form_frame, text="Soft Skills:")
        soft_skills_label.grid(row=4, column=0, sticky="W")
        self.soft_skills_entry = ttk.Entry(self.form_frame)
        self.soft_skills_entry.grid(row=4, column=1, sticky="EW")

        # Hard Skills
        hard_skills_label = ttk.Label(self.form_frame, text="Hard Skills:")
        hard_skills_label.grid(row=5, column=0, sticky="W")
        self.hard_skills_entry = ttk.Entry(self.form_frame)
        self.hard_skills_entry.grid(row=5, column=1, sticky="EW")

        # Trabalho em Equipe
        team_work_label = ttk.Label(self.form_frame, text="Trabalho em Equipe:")
        team_work_label.grid(row=6, column=0, sticky="W")
        self.team_work_entry = ttk.Entry(self.form_frame)
        self.team_work_entry.grid(row=6, column=1, sticky="EW")

        # Resolução de Problemas
        problem_solving_label = ttk.Label(self.form_frame, text="Resolução de Problemas:")
        problem_solving_label.grid(row=7, column=0, sticky="W")
        self.problem_solving_entry = ttk.Entry(self.form_frame)
        self.problem_solving_entry.grid(row=7, column=1, sticky="EW")

        # Configurar redimensionamento
        self.root.columnconfigure(0, weight=1)
        self.form_frame.columnconfigure(1, weight=1)

    def create_buttons(self):
        # Botões
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.grid(row=1, column=0, sticky="EW")

        import_button = ttk.Button(button_frame, text="Importar Candidatos", command=self.set_candidates)
        import_button.grid(row=0, column=0, sticky="EW")

        add_button = ttk.Button(button_frame, text="Adicionar Candidato", command=self.add_candidate)
        add_button.grid(row=0, column=1, sticky="EW")

        generate_button = ttk.Button(button_frame, text="Gerar Classificação", command=self.generate_classification)
        generate_button.grid(row=0, column=2, sticky="EW")

        button_frame.columnconfigure((0, 1, 2), weight=1)

    def add_candidate(self):
        # Obter os valores dos campos
        name = self.name_entry.get()
        age = self.age_entry.get()
        email = self.email_entry.get()
        experience = self.experience_entry.get()
        soft_skills = self.soft_skills_entry.get()
        hard_skills = self.hard_skills_entry.get()
        team_work = self.team_work_entry.get()
        problem_solving = self.problem_solving_entry.get()

        # Validar os campos
        if not name or not age or not email or not experience or not soft_skills or not hard_skills or not team_work or not problem_solving:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        try:
            # Criar os objetos
            person = Person(name, int(age), email)
            candidate = Candidate(
                person, 
                experience, 
                soft_skills, 
                hard_skills, 
                team_work, 
                problem_solving
            )
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser numérica!")
            return

        # Adicionar o candidato à lista
        self.candidates.append(candidate)

        # Limpar os campos
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.experience_entry.delete(0, tk.END)
        self.soft_skills_entry.delete(0, tk.END)
        self.hard_skills_entry.delete(0, tk.END)
        self.team_work_entry.delete(0, tk.END)
        self.problem_solving_entry.delete(0, tk.END)

        messagebox.showinfo("Sucesso", "Candidato adicionado com sucesso!")

    def generate_classification(self):
        if not self.candidates:
            messagebox.showerror("Erro", "Nenhum candidato cadastrado!")
            return

        classifier = Classifier(self.candidates)
        classification = classifier.classify()
        
        categorized_candidates = {
            "Aprovado": [],
            "Aprovado Parcialmente": [],
            "Reprovado": []
        }

        # Distribuir os candidatos nas categorias
        for idx, candidate in enumerate(self.candidates):
            result = classification[idx]
            categorized_candidates[result].append(candidate)

        # Exibir os resultados em uma nova janela
        result_window = tk.Toplevel(self.root)
        result_window.title("Resultados da Classificação")

        text = tk.Text(result_window, wrap=tk.WORD)
        
        for category in ["Aprovado", "Aprovado Parcialmente", "Reprovado"]:
            text.insert(tk.END, f"{category}:\n")
            for candidate in categorized_candidates[category]:
                text.insert(
                    tk.END, 
                    f"  - {candidate.person_record.name} ({candidate.person_record.email})\n"
                )
            text.insert(tk.END, "\n")  # Separar as categorias com uma linha vazia

        text.pack(fill=tk.BOTH, expand=True)

    def run(self):
        self.root.mainloop()
