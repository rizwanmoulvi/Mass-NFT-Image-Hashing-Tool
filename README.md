Mass-Image-Hashing-Tool-For-NFT-Provenance

ABOUT :

Mass Image Hashing Tool For NFT Provenance is developed to ease the process of building provenance for a NFT project. BTW you can use it for other purposes apart from NFT provenance. Hash thousands of NFT images within seconds, and get an concatenated hash and a final hash according to the starting index obtained from the smart contract. Provenance enhances the fair distribution of NFT tokens. 

INFO :

The provenance record of each NFT that will ever exist. Each NFT image is firstly hashed using SHA-256 algorithm. A combined string is obtained by concatenating SHA-256 of each NFT image in the specific order as listed below. The final proof is obtained by SHA-256 hashing this combined string. This is the final provenance record stored on the smart contract.
Each NFT token ID is assigned to an artwork image from the initial sequence with this formula
(tokenId + startingIndex) % 10000 → Initial Sequence Index

REQUIREMENTS :

OS MODULE - PYTHON

HASHLIB MODULE - PYTHON

WORKING :
1. Change images in the "Tool" directory.
2. Get the starting index from smart contract. 
3. Set starting index in Tool.
4. Run the tool.
5. Use the Outputs.
6. Store the final hash in the smart contract.

Process :
1. Clone This Repo
2. Deploy Your Smart Contract With Provenance Functonality To The Blockchain
3. Get Starting Index From The Smart COntract
4. Update Starting Index In The Tool
5. Run The Tool



😇 HAPPY HASHING 🤞

