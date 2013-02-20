import colander
import deform

from trumpet.resources import MemoryTmpStore

phone_re = '\((?P<areacode>[1-9][0-9][0-9])\)-(?P<prefix>[0-9][0-9][0-9])-(?P<suffix>[0-9][0-9][0-9][0-9])'

tmpstore = MemoryTmpStore()

def deferred_choices(node, kw):
    choices = kw['choices']
    return deform.widget.SelectWidget(values=choices)

def make_select_widget(choices):
    return deform.widget.SelectWidget(values=choices)


class AddContactSchema(colander.Schema):
    firstname = colander.SchemaNode(
        colander.String(),
        title='First Name',
        missing=colander.null,
        )
    lastname = colander.SchemaNode(
        colander.String(),
        title='Last Name',
        missing=colander.null,
        )
    email = colander.SchemaNode(
        colander.String(),
        validator=colander.Email(),
        title='Email Address',
        )
    phone = colander.SchemaNode(
        colander.String(),
        title='Phone Number',
        widget=deform.widget.TextInputWidget(mask='(999)-999-9999',
                                      mask_placeholder='0'),
        missing=colander.null,
        )
    

# FIXME!! CHANGE PASSWORD VALIDATOR
class ChangePasswordSchema(colander.Schema):
    oldpass = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(min=1, max=100),
        widget=deform.widget.PasswordWidget(size=20),
        description="Please enter your password.")
    newpass = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(min=1, max=100),
        widget=deform.widget.PasswordWidget(size=20),
        description="Please enter a new password.")
    confirm = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(min=1, max=100),
        widget=deform.widget.PasswordWidget(size=20),
        description="Please confirm the new password.")


class AddressSchema(colander.MappingSchema):
    street = colander.SchemaNode(
        colander.String(),
        title='Street',
        )
    #street2 = colander.SchemaNode(
    #    colander.String(),
    #    title = '',
    #    )
    city = colander.SchemaNode(
        colander.String(),
        title = 'City',
        )
    state = colander.SchemaNode(
        colander.String(),
        title = 'State',
        )
    zip = colander.SchemaNode(
        colander.String(),
        title = 'Zip Code',
        )

