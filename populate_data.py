import random
import csv
from datetime import datetime, timedelta

# List of fictitious products
products = [
    "camisa térmica", "panela de pressão", "livro de receitas", "smartphone", 
    "fones de ouvido", "notebook", "tablet", "cadeira ergonômica", "geladeira", 
    "micro-ondas", "liquidificador", "câmera fotográfica", "conjunto de panelas", 
    "TV LED", "aspirador de pó", "ventilador", "máquina de lavar", "air fryer", 
    "fritadeira elétrica", "batedeira", "bicicleta", "suporte para TV", 
    "smartwatch", "macaquinho de ginástica", "equipamento de musculação", "espremedor de frutas", 
    "cafeteira", "secador de cabelo", "penteadeira", "tênis esportivo", "capa para celular", 
    "carregador portátil", "brinquedo educativo", "cadeira de rodas", "cadeira de balanço", 
    "espelho", "almofada decorativa", "manta de sofá", "sofá", "estante", "mesa de jantar", 
    "cadeira de escritório", "armário", "guarda-roupa", "piscina de plástico", "sacola de praia", 
    "parafusadeira", "extensão elétrica", "banco de jardim", "pedal para bicicleta", 
    "tenda para camping", "lanterna de emergência", "saco de dormir", "tênis de caminhada", 
    "cozinha completa", "organizador de gaveta", "kit de ferramentas", "kit de costura", 
    "poltrona reclinável", "tapete de entrada", "cortina para sala", "luminária", "abajur", 
    "coifa de cozinha", "escada dobrável", "ventilador de coluna", "mesa de centro", 
    "carrinho de bebê", "cadeirinha para carro", "livro de romance", "livro de mistério", 
    "jogo de tabuleiro", "guitarra", "violão", "piano", "saxofone", "trompete", "carro", 
    "moto", "skate", "patins", "bola de futebol", "bola de basquete", "bola de vôlei", 
    "luva de boxe", "colete salva-vidas", "óculos de sol", "mochila de viagem", 
    "jaqueta de couro", "blusa de frio", "chapéu", "barraca de camping", "painel solar", 
    "roçadeira", "serra elétrica", "planta ornamental", "cadeira de praia", "pescaria", 
    "relógio de parede", "porta-retratos", "joias", "bijuterias", "filtro de água", 
    "móveis para jardim", "bolsa de viagem", "cadeira gamer", "cadeira de praia", 
    "assento sanitário", "papel higiênico", "detergente", "sabão em pó", "produto de limpeza"
]

# Function to generate fictional sales data
def generate_sales(start_date, days):
    start_date_obj = datetime.strptime(start_date, "%d/%m/%Y")
    sales = []
    
    # Track the days products were sold
    products_sold = {product: [] for product in products}

    for i in range(days):
        current_date = start_date_obj + timedelta(days=i)
        formatted_date = current_date.strftime("%d/%m/%Y")
        
        # Randomly select products for that day
        daily_products = random.sample(products, random.randint(80, 100))  # between 80 and 100 products
        
        for product in daily_products:
            # Ensure the product isn't repeated on the same day
            while formatted_date in products_sold[product]:
                product = random.choice([p for p in products if formatted_date not in products_sold[p]])
            
            # Generate random quantity of sales between 1 and 100
            quantity_sold = random.randint(1, 100)
            
            # Add the sale to the data
            sales.append([formatted_date, product, quantity_sold])
            # Mark the product as sold on this day
            products_sold[product].append(formatted_date)
            
    return sales

# Generate sales for the next year
sales_data = generate_sales("01/01/2025", 365)

# Write to CSV file
csv_file = 'random_sales_products.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Product", "Sales"])
    writer.writerows(sales_data)

print(f'CSV file generated successfully: {csv_file}')
