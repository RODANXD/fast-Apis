from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Float, ForeignKey, Date
from app.database import Base
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(50))
    lastName = Column(String(50))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    country = Column(String(50))
    role = Column(String(20))
    isDeleted = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP)

class TransactionHistory(Base):
    __tablename__ = 'transaction_history'

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer)
    paymentId = Column(String(100), nullable=False)
    amountPaid = Column(Float, nullable=False)
    email = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    paymentMethod = Column(String(50))
    subscriptionType = Column(String(20))
    receiptUrl = Column(String(255))
    currency = Column(String)
    transactionDate = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)

class Teammembers(Base):
    __tablename__ = 'teammembers'

    id = Column(Integer, primary_key=True, index=True)
    isAdmin = Column(Boolean, nullable=True)
    role = Column(String(20), nullable=False)
    teamId = Column(String, nullable=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    
    # Relationship with User model
    user = relationship("User", backref="team_members", lazy="joined")


class Team(Base):
    __tablename__ = 'team'

    id = Column(String, primary_key=True)
    userId = Column(Integer, nullable=True)
    numberOfTeamMembers = Column(Integer, nullable=True)
    credits = Column(Integer, nullable=True)


class AgentPhoneNumber(Base):
    __tablename__ = "agent_phone_numbers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)  
    status = Column(Boolean, nullable=True)
    number_type = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", backref="agent_phone_numbers", lazy="joined")


class AppointmentSetter(Base):

    
    __tablename__ = "appointment_setter"
    id = Column(Integer, primary_key=True, index=True)
    agent_name = Column(String, nullable=False)
    agent_personality = Column(String, nullable=False)
    agent_language = Column(ARRAY(String), nullable=True)               
    gender = Column(String, nullable=True)
    age = Column(Integer, nullable=False)
    business_description = Column(String, nullable=False)
    your_business_offer = Column(String, nullable=False)
    qualification_questions = Column(ARRAY(String), nullable=True)     
    sequence = Column(JSONB, nullable=False)                            
    objective_of_the_agent = Column(String, nullable=False)
    calendar_choosed = Column(String, nullable=True)
    calendar_id = Column(String, nullable=True)
    webpage_link = Column(String, nullable=True)
    whatsapp_number = Column(String, nullable=True)
    prompt = Column(String, nullable=False)
    platform_unique_id = Column(String, nullable=False)
    is_followups_enabled = Column(Boolean, nullable=True)
    follow_up_details = Column(JSONB, nullable=True)                    
    emoji_frequency = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    first_message = Column(String, nullable=True)
    user = relationship("User", backref="appointment_setter", lazy="joined")


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String, nullable=True)
    lastName = Column(String, nullable=True)
    businessName = Column(String, nullable=True)
    companyName = Column(String, nullable=True)
    countryCode = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    created = Column(String, nullable=True)         
    lastActivity = Column(String, nullable=True)    
    status = Column(String, nullable=True)
    tags = Column(String, nullable=True)
    additionalEmails = Column(String, nullable=True)
    additionalPhones = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    team_id = Column(String, nullable=True)


class ContactList(Base):
    __tablename__ = "contact_lists"

    id = Column(Integer, primary_key=True, index=True)
    contactid = Column(Integer, ForeignKey("contacts.id"), nullable=True)
    lists_id = Column(Integer, nullable=True)  
    contact = relationship("Contact", backref="contact_lists", lazy="joined")


class Lists(Base):
    __tablename__ = 'lists'

    id = Column(Integer, primary_key=True, index=True)
    listName = Column(String, nullable=True)
    channel = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    team_id = Column(String, nullable=True)
    description = Column(String, nullable=True)


class Lead_Analytics(Base):

    __tablename__ = 'lead_analytics'
    id = Column(Integer, primary_key=True, index=True)
    chat_history = Column(ARRAY(JSONB), nullable=True)  
    thread_id = Column(String, nullable=True)
    agent_id = Column(Integer, nullable=True)           
    lead_id = Column(Integer, nullable=True)            
    agent_is_enabled = Column(Boolean, nullable=True)
    status = Column(String, nullable=True)
    platform_unique_id = Column(String, nullable=True)
    created_at = Column(Date, nullable=True)
    updated_at = Column(Date, nullable=True)


class InviteTokens(Base):
    __tablename__ = 'invite_tokens'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False)
    token = Column(String(255), nullable=False, unique=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=True)
    teamId = Column(String, ForeignKey("team.id"), nullable=True)
    role = Column(String, nullable=True)
    expiresAt = Column(TIMESTAMP, nullable=False)
    accepted = Column(Boolean, nullable=True, default=False)
    created_at = Column(TIMESTAMP, nullable=True)



class PhoneAgent(Base):

    __tablename__ = 'phone_agent'

    id = Column(Integer, primary_key=True, index=True)
    agent_name = Column(String, nullable=False)
    language = Column(String, nullable=False)
    status = Column(Boolean, nullable=True)
    voice = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", backref="phone_agents", lazy="joined")


class PhoneCampaign(Base):

    __tablename__ =  "phone_campaign"

    id = Column(Integer, primary_key=True, index=True)
    campaign_name = Column(String, nullable=False)
    language = Column(String, nullable=False)
    voice = Column(String, nullable=False)
    choose_calendar = Column(String, nullable=True)
    max_call_time = Column(Integer, nullable=True)
    country = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    status = Column(String, nullable=True)
    catch_phrase = Column(String, nullable=False)
    call_script = Column(String, nullable=False)
    tom_engages = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, nullable=True)
    agent = Column(Integer, nullable=True)     
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    target_lists = Column(Integer, nullable=False)


class EmailCampaign(Base):
    __tablename__ = "email_campaign"

    id = Column(Integer, primary_key=True, index=True)
    campaign_title = Column(String, nullable=False)
    campaign_objective = Column(String, nullable=False)
    main_subject = Column(String, nullable=False)
    cta_type = Column(String, nullable=False)
    list_of_target = Column(ARRAY(Integer), nullable=False)
    desired_tone = Column(String, nullable=False)
    language = Column(String, nullable=False)
    send_time_window = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    frequency = Column(ARRAY(String), nullable=True)
    include_brainai = Column(Boolean, default=False)
    include_branding = Column(Boolean, default=False)
    custom_prompt = Column(String, nullable=True)
    text_length = Column(String, nullable=False)
    product_or_service_feature = Column(String, nullable=False)
    review = Column(Boolean, default=False)
    calender_choosed = Column(String, nullable=True)
    url = Column(String, nullable=False)
    is_draft = Column(Boolean, default=False)
    status = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)



class LinkedInPost(Base):
    __tablename__ = "linkedin_post"

    id = Column(Integer, primary_key=True, index=True)
    generated_content = Column(String, nullable=False)
    topic = Column(String, nullable=False)
    tone = Column(String, nullable=False)
    custom_instructions = Column(String, nullable=True)
    prompt = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False)
    user = Column(Integer, ForeignKey("users.id"), nullable=True)


class ScheduledContent(Base):
    __tablename__ = 'scheduled_content'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    document = Column(String, nullable=True)
    platform = Column(String, nullable=False)
    platform_unique_id = Column(String, nullable=False)
    scheduled_type = Column(String, nullable=False)
    scheduled_date = Column(Date, nullable=True)
    scheduled_time = Column(String, nullable=True)
    published_time = Column(TIMESTAMP, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    media_type = Column(String, nullable=False)
    media_id = Column(String, nullable=True)
    user = relationship("User", backref="scheduled_contents", lazy="joined")


class WhatsAppConnection(Base):
    __tablename__ = 'whatsapp_connection_details'

    whatsapp_business_id = Column(String, primary_key=True)
    whatsapp_phone_id = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    name = Column(String, nullable=True)
    access_token = Column(String, nullable=False)
    expiry_time = Column(TIMESTAMP, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", backref="whatsapp_connections", lazy="joined")