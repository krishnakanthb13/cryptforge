from logics.base import EncryptionLogic


class PolybiusSquareLogic(EncryptionLogic):
    SQUARE = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # I/J combined

    @property
    def name(self) -> str:
        return "polybius"

    @property
    def description(self) -> str:
        return "Polybius square cipher (5x5 grid)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        text = data.decode('utf-8', errors='replace').upper().replace('J', 'I')
        result = []
        for c in text:
            if c in self.SQUARE:
                idx = self.SQUARE.index(c)
                result.append(f"{idx // 5 + 1}{idx % 5 + 1}")
            else:
                result.append(c)
        return ' '.join(result).encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        parts = data.decode('utf-8', errors='replace').split()
        result = []
        for p in parts:
            if len(p) == 2 and p.isdigit():
                row, col = int(p[0]) - 1, int(p[1]) - 1
                if 0 <= row < 5 and 0 <= col < 5:
                    result.append(self.SQUARE[row * 5 + col])
                else:
                    result.append(p)
            else:
                result.append(p)
        return ''.join(result).encode('utf-8')


class TapCodeLogic(EncryptionLogic):
    GRID = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # K replaces C, no J

    @property
    def name(self) -> str:
        return "tapcode"

    @property
    def description(self) -> str:
        return "Tap code (Prisoners' cipher)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        text = data.decode('utf-8', errors='replace').upper().replace('K', 'C').replace('J', 'I')
        result = []
        for c in text:
            if c in self.GRID:
                idx = self.GRID.index(c)
                row, col = idx // 5 + 1, idx % 5 + 1
                result.append('.' * row + ' ' + '.' * col)
            elif c == ' ':
                result.append('/')
        return ' '.join(result).encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        parts = data.decode('utf-8', errors='replace').split(' ')
        result = []
        i = 0
        while i < len(parts):
            if parts[i] == '/':
                result.append(' ')
                i += 1
            elif i + 1 < len(parts) and parts[i].replace('.', '') == '' and parts[i + 1].replace('.', '') == '':
                row = len(parts[i]) - 1
                col = len(parts[i + 1]) - 1
                if 0 <= row < 5 and 0 <= col < 5:
                    result.append(self.GRID[row * 5 + col])
                i += 2
            else:
                i += 1
        return ''.join(result).encode('utf-8')


class BifidCipherLogic(EncryptionLogic):
    SQUARE = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    @property
    def name(self) -> str:
        return "bifid"

    @property
    def description(self) -> str:
        return "Bifid cipher (fractionation)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        text = data.decode('utf-8', errors='replace').upper().replace('J', 'I')
        text = ''.join(c for c in text if c in self.SQUARE)
        rows, cols = [], []
        for c in text:
            idx = self.SQUARE.index(c)
            rows.append(idx // 5)
            cols.append(idx % 5)
        combined = rows + cols
        result = []
        for i in range(0, len(combined), 2):
            if i + 1 < len(combined):
                result.append(self.SQUARE[combined[i] * 5 + combined[i + 1]])
        return ''.join(result).encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        text = data.decode('utf-8', errors='replace').upper()
        text = ''.join(c for c in text if c in self.SQUARE)
        coords = []
        for c in text:
            idx = self.SQUARE.index(c)
            coords.append(idx // 5)
            coords.append(idx % 5)
        mid = len(coords) // 2
        rows, cols = coords[:mid], coords[mid:]
        result = []
        for r, c in zip(rows, cols):
            result.append(self.SQUARE[r * 5 + c])
        return ''.join(result).encode('utf-8')


class TrifidCipherLogic(EncryptionLogic):
    CUBE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ+'  # 27 chars for 3x3x3

    @property
    def name(self) -> str:
        return "trifid"

    @property
    def description(self) -> str:
        return "Trifid cipher (3D fractionation)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        text = data.decode('utf-8', errors='replace').upper()
        text = ''.join(c if c in self.CUBE else '+' for c in text if c.isalpha() or c == '+')
        layers, rows, cols = [], [], []
        for c in text:
            idx = self.CUBE.index(c)
            layers.append(idx // 9)
            rows.append((idx % 9) // 3)
            cols.append(idx % 3)
        combined = []
        for l, r, c in zip(layers, rows, cols):
            combined.extend([l, r, c])
        result = []
        for i in range(0, len(combined), 3):
            if i + 2 < len(combined):
                idx = combined[i] * 9 + combined[i + 1] * 3 + combined[i + 2]
                if idx < len(self.CUBE):
                    result.append(self.CUBE[idx])
        return ''.join(result).encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        text = data.decode('utf-8', errors='replace').upper()
        text = ''.join(c for c in text if c in self.CUBE)
        coords = []
        for c in text:
            idx = self.CUBE.index(c)
            coords.extend([idx // 9, (idx % 9) // 3, idx % 3])
        n = len(text)
        layers = coords[:n]
        rows = coords[n:2 * n]
        cols = coords[2 * n:3 * n]
        result = []
        for l, r, c in zip(layers, rows, cols):
            result.append(self.CUBE[l * 9 + r * 3 + c])
        return ''.join(result).encode('utf-8')


class ADFGXCipherLogic(EncryptionLogic):
    SQUARE = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # I/J combined
    LABELS = 'ADFGX'

    @property
    def name(self) -> str:
        return "adfgx"

    @property
    def description(self) -> str:
        return "ADFGX cipher (Polybius + Transposition)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        if not password:
             raise ValueError("Password is required for ADFGX")
        
        # 1. Polybius Substitution
        text = data.decode('utf-8', errors='replace').upper().replace('J', 'I')
        fractionated = []
        for c in text:
            if c in self.SQUARE:
                idx = self.SQUARE.index(c)
                row, col = idx // 5, idx % 5
                fractionated.append(self.LABELS[row] + self.LABELS[col])
        
        fractionated_str = ''.join(fractionated)
        if not fractionated_str:
            return b""

        # 2. Columnar Transposition
        key = password.upper()
        # Remove duplicates from key for column ordering? Standard ADFGX usually implies unique key chars or standard sort logic.
        # We'll use standard columnar transposition logic:
        # Create grid with width = len(key)
        
        # Sort key to determine column read order
        # If key has duplicates, we keep original order of occurrence or sort? 
        # Standard: sort key chars. If duplicates, use standard stable sort.
        key_indices = sorted(range(len(key)), key=lambda k: key[k])
        
        cols = [''] * len(key)
        for i, char in enumerate(fractionated_str):
            col_idx = i % len(key)
            cols[col_idx] += char
            
        # Read off columns in sorted key order
        result = []
        for i in key_indices:
            result.append(cols[i])
            
        return ' '.join(result).encode('utf-8') # Space separated for readability? Or combined. Standard is grouped. I'll group by space.

    def decrypt(self, data: bytes, password: str) -> bytes:
        if not password:
            raise ValueError("Password is required")
            
        ciphertext = data.decode('utf-8', errors='replace').replace(' ', '')
        key = password.upper()
        L = len(ciphertext)
        K = len(key)
        
        # Calculate column lengths
        # N full columns, M remainder
        num, rem = divmod(L, K)
        
        # Determine column lengths based on key index
        # Columns 0..rem-1 get num+1 chars, others get num chars?
        # Only if we filled 0..K. We filled row by row.
        # So yes, first 'rem' columns in the original grid (0..rem-1) have num+1.
        
        col_lengths = [num + 1 if i < rem else num for i in range(K)]
        
        # But we must associate these lengths with the SORTED key columns.
        # Wait. When encrypting, we filled col 0, 1, 2... sequentially row by row.
        # Then we read out based on sorted key.
        # So if key is encryption order, say key="BAC":
        # Indices: B(0), A(1), C(2). Sorted: A(1), B(0), C(2).
        # We read col 1, then col 0, then col 2.
        # To decrypt, we have the ciphertext which is col 1 + col 0 + col 2.
        # We need to cut it into chunks.
        # The length of col 1 depends on its original index (1).
        # The length of col 0 depends on its original index (0).
        
        key_indices = sorted(range(K), key=lambda k: key[k])
        
        # Reconstruct columns
        cols = [''] * K
        start = 0
        for k_idx in key_indices:
            # How long is this column? It corresponds to original index k_idx
            length = col_lengths[k_idx]
            cols[k_idx] = ciphertext[start:start+length]
            start += length
            
        # Read off row by row
        plain_fragment = []
        # Max length of any column is num+1
        max_len = num + 1 if rem > 0 else num
        for row in range(max_len):
            for col_idx in range(K):
                if row < len(cols[col_idx]):
                    plain_fragment.append(cols[col_idx][row])
                    
        fractionated_str = ''.join(plain_fragment)
        
        # Reverse Polybius
        result = []
        for i in range(0, len(fractionated_str), 2):
            if i+1 < len(fractionated_str):
                r_char = fractionated_str[i]
                c_char = fractionated_str[i+1]
                if r_char in self.LABELS and c_char in self.LABELS:
                    r = self.LABELS.index(r_char)
                    c = self.LABELS.index(c_char)
                    result.append(self.SQUARE[r*5 + c])
                    
        return ''.join(result).encode('utf-8')


class NihilistCipherLogic(EncryptionLogic):
    SQUARE = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # I/J combined

    @property
    def name(self) -> str:
        return "nihilist"

    @property
    def description(self) -> str:
        return "Nihilist cipher (Polybius + Key addition)"

    def _get_coords(self, text: str):
        coords = []
        for c in text:
            if c in self.SQUARE:
                idx = self.SQUARE.index(c)
                # Polybius 11-55
                val = (idx // 5 + 1) * 10 + (idx % 5 + 1)
                coords.append(val)
        return coords

    def encrypt(self, data: bytes, password: str) -> bytes:
        if not password:
             raise ValueError("Password required")
        
        text = data.decode('utf-8', errors='replace').upper().replace('J', 'I')
        # Get coordinates for plaintext
        plain_coords = self._get_coords(text)
        
        # Get coordinates for key
        key = password.upper().replace('J','I')
        key_coords = self._get_coords(key)
        if not key_coords:
             # Fallback key if invalid chars
             key_coords = [11] 
             
        # Add them
        result = []
        k_len = len(key_coords)
        for i, val in enumerate(plain_coords):
             k_val = key_coords[i % k_len]
             result.append(str(val + k_val))
             
        return ' '.join(result).encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        if not password:
             raise ValueError("Password required")
             
        parts = data.decode('utf-8', errors='replace').split()
        key = password.upper().replace('J','I')
        key_coords = self._get_coords(key)
        if not key_coords:
             key_coords = [11]
             
        k_len = len(key_coords)
        result = []
        
        # Reverse mapping for coords to char
        # e.g. 11 -> A
        rev_square = {}
        for idx, char in enumerate(self.SQUARE):
             val = (idx // 5 + 1) * 10 + (idx % 5 + 1)
             rev_square[val] = char
             
        for i, p in enumerate(parts):
            try:
                # Cipher value = plain + key
                # plain = cipher - key
                c_val = int(p)
                k_val = key_coords[i % k_len]
                plain_val = c_val - k_val
                
                if plain_val in rev_square:
                    result.append(rev_square[plain_val])
                else:
                    # Should not happen in valid cipher, maybe output '?' or raw
                    result.append('?') 
            except ValueError:
                pass
                
        return ''.join(result).encode('utf-8')

