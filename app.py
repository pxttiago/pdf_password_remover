import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter

class RemovedorSenhaPDF:
    def __init__(self, master):
        self.master = master
        master.title("Removedor de Senha para PDF")

        # Container principal
        self.container_principal = tk.Frame(master)
        self.container_principal.pack(padx=20, pady=20)

        # Label
        self.label = tk.Label(self.container_principal, text="Removedor de Senha para PDF", font=('Helvetica', 16))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        # Campo de seleção de arquivo PDF
        self.arquivo_var = tk.StringVar()
        self.arquivo_entry = tk.Entry(self.container_principal, textvariable=self.arquivo_var, state='disabled', width=30)
        self.arquivo_entry.grid(row=1, column=0, padx=5, pady=10, sticky='ew')
        self.selecionar_arquivo_botao = tk.Button(self.container_principal, text="Selecionar Arquivo", command=self.selecionar_arquivo)
        self.selecionar_arquivo_botao.grid(row=1, column=1, padx=5, pady=10, sticky='ew')

        # Campo de senha
        self.senha_var = tk.StringVar()
        self.senha_label = tk.Label(self.container_principal, text="Senha:")
        self.senha_label.grid(row=2, column=0, padx=5, pady=10, sticky='e')
        self.senha_entry = tk.Entry(self.container_principal, textvariable=self.senha_var, show='*')
        self.senha_entry.grid(row=2, column=1, padx=5, pady=10, sticky='ew', columnspan=2)

        # Botão de remover senha
        self.remover_senha_botao = tk.Button(self.container_principal, text="Remover Senha", command=self.remover_senha)
        self.remover_senha_botao.grid(row=3, column=0, columnspan=3, pady=10)

    def selecionar_arquivo(self):
        arquivo = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf"), ("Todos os Arquivos", "*.*")])
        if arquivo:
            self.arquivo_var.set(arquivo)

    def remover_senha(self):
        arquivo_pdf = self.arquivo_var.get()
        senha = self.senha_var.get()

        if not arquivo_pdf:
            messagebox.showerror("Erro", "Por favor, selecione um arquivo PDF.")
            return

        reader = PdfReader(arquivo_pdf)
        writer = PdfWriter()

        try:
            if reader.is_encrypted:
                reader.decrypt(senha)

            for page in reader.pages:
                writer.add_page(page)

            novo_arquivo_pdf = arquivo_pdf.replace(".pdf", "_sem_senha.pdf")

            with open(novo_arquivo_pdf, 'wb') as novo_pdf:
                writer.write(novo_pdf)

            messagebox.showinfo("Sucesso", "Senha removida com sucesso. Novo arquivo salvo em:\n{}".format(novo_arquivo_pdf))

        except Exception as e:
            messagebox.showerror("Erro", "Ocorreu um erro ao remover a senha. Verifique a senha e tente novamente.\n{}".format(str(e)))

if __name__ == "__main__":
    root = tk.Tk()
    removedor_senha_pdf = RemovedorSenhaPDF(root)
    root.mainloop()

