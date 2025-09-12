# 🛠️ Technical & Code Prompts

Boost your development workflow with these programming and technical prompts.

## Code Review & Quality

### 🔍 Code Review Checklist Generator
**Prompt:**
```
Create a 5-point code review checklist for [LANGUAGE/FRAMEWORK] focusing on the most critical issues that lead to bugs in production.
```

**Sample Result:**
**Language: Python/Django**

1. **Security**: SQL injection prevention (use ORM, parameterized queries), XSS protection (escape user input), authentication/authorization checks
2. **Error Handling**: Try-catch blocks around external API calls, database operations, and file I/O; meaningful error messages for debugging
3. **Performance**: N+1 query detection, unnecessary loops in templates, large data set pagination, proper database indexing
4. **Testing**: Unit tests for business logic, integration tests for API endpoints, edge case coverage (empty data, invalid input)
5. **Configuration**: Environment variables for secrets, database migrations included, proper logging levels set

### 🐛 Debug Strategy Framework
**Prompt:**
```
I'm getting [ERROR/ISSUE]. Give me a systematic 4-step debugging approach starting with the fastest checks.
```

**Sample Result:**
**Issue: "API returns 500 error intermittently"**

**4-Step Debug Strategy:**
1. **Quick Checks (5 min)**: Check server logs for specific error messages, verify API endpoint is correct, test with simple request (Postman/curl)
2. **Data Validation (10 min)**: Log incoming request data, check for null/empty values, validate data types match API expectations
3. **Environment Issues (15 min)**: Check database connections, verify third-party service availability, review recent deployments/config changes
4. **Load & Timing (20 min)**: Test with different request volumes, check for race conditions, analyze response times under load

## Documentation & Comments

### 📝 Function Documentation Generator
**Prompt:**
```
Write clear documentation for this function that explains what it does, parameters, return value, and includes a usage example: [CODE FUNCTION]
```

**Sample Result:**
**Function:** `calculateDiscount(price, customerType, itemCategory)`

```python
def calculateDiscount(price, customerType, itemCategory):
    """
    Calculate the discount amount for a customer purchase.
    
    Applies tiered discounts based on customer type and item category.
    
    Args:
        price (float): Original price of the item (must be > 0)
        customerType (str): Customer category ('regular', 'premium', 'vip')
        itemCategory (str): Item type ('electronics', 'clothing', 'books')
    
    Returns:
        float: Discount amount to subtract from original price
        
    Example:
        >>> calculateDiscount(100.0, 'premium', 'electronics')
        15.0  # 15% discount for premium customer buying electronics
    """
```

### 📋 README Template Creator
**Prompt:**
```
Create a professional README template for a [PROJECT TYPE] that covers all essential sections without being overwhelming.
```

**Sample Result:**
**Project Type: Python CLI Tool**

```markdown
# Project Name

Brief description of what your tool does and why it's useful.

## Installation

```bash
pip install your-tool-name
```

## Quick Start

```bash
your-tool --help
your-tool [basic-command]
```

## Usage Examples

```bash
# Common use case 1
your-tool --option value

# Common use case 2  
your-tool --different-option
```

## Configuration

Optional config file location and format.

## Contributing

1. Fork the repo
2. Create feature branch
3. Submit pull request

## License

MIT License - see LICENSE file.
```

## Testing & Debugging

### 🧪 Test Case Generator
**Prompt:**
```
Generate test cases for [FUNCTION/FEATURE] covering: happy path, edge cases, and error conditions. Include expected results.
```

**Sample Result:**
**Function: validateEmail(email)**

```python
# Happy Path
def test_valid_emails():
    assert validateEmail("user@example.com") == True
    assert validateEmail("test.email+tag@domain.co.uk") == True

# Edge Cases  
def test_edge_cases():
    assert validateEmail("a@b.co") == True  # Minimum valid email
    assert validateEmail("very.long.email.address@very.long.domain.name.com") == True

# Error Conditions
def test_invalid_emails():
    assert validateEmail("") == False  # Empty string
    assert validateEmail("notanemail") == False  # No @ symbol
    assert validateEmail("@domain.com") == False  # Missing username
    assert validateEmail("user@") == False  # Missing domain
    assert validateEmail(None) == False  # Null input
```

### 🔧 Performance Optimization Checker
**Prompt:**
```
Analyze this code for performance issues: [CODE SNIPPET]. Suggest the top 3 improvements with estimated impact.
```

**Sample Result:**
**Code: Database query in loop**

```python
# Original code
users = User.objects.all()
for user in users:
    profile = Profile.objects.get(user_id=user.id)  # N+1 query!
    print(f"{user.name}: {profile.bio}")
```

**Top 3 Improvements:**
1. **Use select_related() for JOIN** (90% faster)
   ```python
   users = User.objects.select_related('profile').all()
   for user in users:
       print(f"{user.name}: {user.profile.bio}")
   ```

2. **Batch process in chunks** (Reduces memory usage by 80%)
   ```python
   for users_batch in User.objects.select_related('profile').iterator(chunk_size=1000):
   ```

3. **Add database indexing** (50% faster queries)
   ```python
   # In model
   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=CASCADE, db_index=True)
   ```

---

*Want to contribute more technical prompts? Check out our [Contributing Guide](../CONTRIBUTING.md)!*