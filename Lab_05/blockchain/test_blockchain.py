from blockchain import Blockchain

# Tạo blockchain
my_blockchain = Blockchain()

# Nhập dữ liệu giao dịch từ người dùng
while True:
    sender = input("Nhập người gửi (hoặc 'dừng' để kết thúc): ")
    if sender.lower() == 'dừng':
        break
    receiver = input("Nhập người nhận: ")
    amount = float(input("Nhập số tiền giao dịch: "))
    
    # Thêm giao dịch vào blockchain
    my_blockchain.add_transaction(sender, receiver, amount)
    print(f"Đã thêm giao dịch: {sender} -> {receiver} | Số tiền: {amount}")

# Khai thác khối mới
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction('Genesis', 'Miner', 1)
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Hiển thị blockchain
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("------------------------------")

# Kiểm tra tính hợp lệ của blockchain
print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
